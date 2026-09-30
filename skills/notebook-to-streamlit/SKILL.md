# notebook-to-streamlit

## Purpose

Convert the analytical logic from the Rosa's Pizza Jupyter Notebook into a Streamlit web application.

The Streamlit application should reuse the analytical logic developed in the notebook instead of creating a different calculation.

## Rosa's Pizza starter package

The application must import:

from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE, delivery_times

Do not recreate, redefine, modify, or hard-code:

- ZONES
- TIME_BLOCKS
- COSTS
- PROMISE
- delivery_times()

These must be imported from the starter package.

## Notebook logic

The student's Part II notebook calculates the net profit for different promised delivery times.

The current notebook uses:

promise_values = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]

For each promised delivery time, the notebook:

1. Gets the delivery times using delivery_times(zone, time_block, promise).
2. Counts late deliveries.
3. Counts total deliveries.
4. Calculates on-time deliveries.
5. Calculates the cost of a late order.
6. Calculates net profit.
7. Stores the result.
8. Identifies the promise with the highest net profit.

The calculation used in the notebook is:

late_deliveries_count = (times > p).sum()

total_deliveries_count = len(times)

on_time_deliveries_count = total_deliveries_count - late_deliveries_count

costs_per_late_order = COSTS['refund'] + COSTS['churn_orders'] * COSTS['margin']

net_profit = (
    on_time_deliveries_count * COSTS['margin']
    - late_deliveries_count * costs_per_late_order
)

The Streamlit application must preserve this analytical logic.

## Streamlit application requirements

The application must allow the user to:

1. Select a zone from a dropdown menu.
2. Select a time block from a dropdown menu.
3. Set the range of promised delivery times to test.
4. Adjust the profit margin per order.
5. Adjust the estimated churn orders per late order.
6. Adjust the refund cost per late order.
7. Click a button to calculate the best promised delivery time.
8. Display the recommended promised delivery time and its net profit.

## Zone selection

The application must use the ZONES variable imported from starter.

Use a Streamlit dropdown such as:

st.selectbox(...)

Do not manually recreate the zone names.

## Time block selection

The application must use the TIME_BLOCKS variable imported from starter.

Use a Streamlit dropdown such as:

st.selectbox(...)

Do not manually recreate the time block names.

## Promise range

The notebook currently uses a fixed list of promised delivery times:

[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]

In the Streamlit application, this list must become user-controlled.

The user should be able to specify:

- minimum promised time
- maximum promised time
- step size

The application should generate the promise values from these inputs.

For example:

promise_values = range(min_promise, max_promise + 1, step)

The application must validate the inputs before performing the calculation.

## Economic assumptions

The default values must come from COSTS.

Use:

margin = COSTS["margin"]

churn_orders = COSTS["churn_orders"]

refund = COSTS["refund"]

The user must be able to modify these three values in the Streamlit application.

The modified values must be used in the net profit calculation.

## Net profit calculation

For every candidate promised delivery time:

1. Generate the delivery times:

times = delivery_times(zone, time_block, promise)

2. Count late deliveries:

late_deliveries_count = (times > promise).sum()

A delivery is considered late when its actual delivery time is greater than the promised delivery time.

3. Count total deliveries:

total_deliveries_count = len(times)

4. Calculate on-time deliveries:

on_time_deliveries_count = (
    total_deliveries_count - late_deliveries_count
)

5. Calculate the cost of one late order:

costs_per_late_order = (
    refund + churn_orders * margin
)

6. Calculate net profit:

net_profit = (
    on_time_deliveries_count * margin
    - late_deliveries_count * costs_per_late_order
)

7. Store the result.

Each result should contain at least:

- zone
- time_block
- promise
- net_profit

## Finding the best promise

The recommended promise is the candidate promise with the highest net profit.

Use logic equivalent to:

best_result = max(
    results,
    key=lambda x: x["net_profit"]
)

The application should display the promise from best_result as the recommended promised delivery time.

It should also display the corresponding net profit.

## Recommended code structure

Keep the analytical calculation separate from the Streamlit interface when practical.

A function such as the following can be used:

def calculate_results(
    zone,
    time_block,
    promise_values,
    margin,
    churn_orders,
    refund
):
    ...

This function should perform the calculations for all candidate promises and return the results.

The Streamlit interface should collect the inputs and call the calculation function when the user clicks the button.

## User interface

The application should have a clear and simple layout suitable for a beginner Python/Streamlit assignment.

The interface should include:

- application title
- zone dropdown
- time block dropdown
- minimum promise input
- maximum promise input
- promise step input
- profit margin input
- churn orders input
- refund cost input
- "Find Best Promise" button

After the calculation, clearly display:

- selected zone
- selected time block
- recommended promised delivery time
- recommended net profit

The recommended promise should be visually prominent.

It is acceptable to additionally display the results for all tested promises in a table or chart, but this is not required.

## Button behavior

The calculation should happen when the user clicks the button.

Do not require the user to enter values using Python input().

Do not use:

input("Enter the zone...")

or

input("Enter the time_block...")

The Streamlit widgets must replace the notebook's input() functions.

## Error handling

The application should not crash if the user enters an invalid promise range.

Check that:

- minimum promise is not greater than maximum promise
- step size is greater than zero
- the generated promise range contains at least one value

Use Streamlit error or warning messages when appropriate.

## Requirements.txt

Create a requirements.txt file containing:

streamlit
numpy
git+https://github.com/zhouy185/rosa-starter.git

The rosa-starter package is required because the application must import the Rosa's Pizza starter variables and delivery_times function.

## Compatibility

The application must be compatible with Streamlit Community Cloud.

Do not use local files, paths, or dependencies that would prevent the application from running after deployment.

## Coding style

Keep the code:

- beginner-friendly
- readable
- clearly organized
- appropriately commented
- consistent with the student's existing Python knowledge

Do not introduce unnecessary advanced programming concepts.

Do not create a completely different analytical approach.

The purpose of this application is to transform the student's existing Part II notebook analysis into an interactive Streamlit decision-support application.

## Final objective

The final application should transform the notebook workflow:

Zone + Time Block + Fixed Promise Values + COSTS
→ Calculate delivery times
→ Count late orders
→ Calculate net profit
→ Find highest net profit

into:

Zone dropdown
+ Time Block dropdown
+ User-defined Promise Range
+ Adjustable Economic Assumptions
→ Calculate delivery times
→ Count late orders
→ Calculate net profit
→ Find highest net profit
→ Display Recommended Promise