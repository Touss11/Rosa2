import streamlit as st

from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE, delivery_times


def calculate_results(
    zone,
    time_block,
    promise_values,
    margin,
    churn_orders,
    refund,
):
    costs_per_late_order = refund + churn_orders * margin
    results = []

    for promise in promise_values:
        times = delivery_times(zone, time_block, promise)
        late_orders = (times > promise).sum()
        total_orders = len(times)
        on_time_orders = total_orders - late_orders
        net_profit = (
            on_time_orders * margin
            - late_orders * costs_per_late_order
        )
        results.append(
            {
                "zone": zone,
                "time_block": time_block,
                "promise": promise,
                "net_profit": net_profit,
            }
        )

    return results


st.set_page_config(page_title="Rosa's Pizza Promise Planner")
st.title("Rosa's Pizza Promise Planner")
st.write("Test delivery promises and find the option with the highest net profit.")

with st.sidebar:
    st.header("Scenario")
    zone = st.selectbox("Zone", ZONES)
    time_block = st.selectbox("Time block", TIME_BLOCKS)

    st.subheader("Promise range")
    min_promise = st.number_input("Minimum promise (minutes)", min_value=1, value=5, step=1)
    max_promise = st.number_input("Maximum promise (minutes)", min_value=1, value=80, step=1)
    promise_step = st.number_input("Step size (minutes)", min_value=1, value=5, step=1)

    st.subheader("Economic assumptions")
    margin = st.number_input(
        "Profit margin per order",
        min_value=0.0,
        value=float(COSTS["margin"]),
        step=0.50,
    )
    churn_orders = st.number_input(
        "Churn orders per late order",
        min_value=0.0,
        value=float(COSTS["churn_orders"]),
        step=0.1,
    )
    refund = st.number_input(
        "Refund cost per late order",
        min_value=0.0,
        value=float(COSTS["refund"]),
        step=0.50,
    )

if st.button("Find Best Promise", type="primary"):
    if min_promise > max_promise:
        st.error("The minimum promise must be less than or equal to the maximum promise.")
    else:
        promise_values = range(min_promise, max_promise + 1, promise_step)
        results = calculate_results(
            zone,
            time_block,
            promise_values,
            margin,
            churn_orders,
            refund,
        )
        best_result = max(results, key=lambda result: result["net_profit"])

        st.subheader("Recommendation")
        result_columns = st.columns(2)
        result_columns[0].metric(
            "Recommended promise",
            f"{best_result['promise']} minutes",
        )
        result_columns[1].metric(
            "Net profit",
            f"${best_result['net_profit']:,.2f}",
        )
        st.caption(f"Zone: {zone} | Time block: {time_block}")
