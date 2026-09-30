import numpy as np
from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE, delivery_times

results = []
promise_values = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
costs_per_late_order = COSTS['refund'] + COSTS['churn_orders']*COSTS['margin']

zone = input("Enter the zone you want to study: ")
time_block = input("Enter the time_block you want to study: ")

for p in promise_values:
  times = delivery_times(zone, time_block, p)
  late_deliveries_count = (times > p).sum()
  total_deliveries_count = len(times)
  on_time_deliveries_count = total_deliveries_count - late_deliveries_count
  net_profit = ((on_time_deliveries_count)*COSTS['margin']) - (late_deliveries_count*costs_per_late_order)
  results.append({"zone": zone, "time_block": time_block, "promise": p, "net_profit": net_profit})

sorted_results = sorted(results, key=lambda x: x['net_profit'], reverse=True)

print("Pairs ranking by net_profit :")
for i, item in enumerate(sorted_results):
  print(f"{i+1}. Zone: {item['zone']}, Time Block: {item['time_block']}, Promise: {item['promise']}, net_profit : {item['net_profit']}")