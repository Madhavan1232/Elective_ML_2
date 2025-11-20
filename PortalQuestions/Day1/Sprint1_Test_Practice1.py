print("BuyBloom Probability Calculator")
order_shipped = int(input("Enter total number of orders shipped: "))
returned_orders = int(input("Enter number of orders returned: "))
not_returned = (order_shipped - returned_orders) / order_shipped
print(f"Probability a randomly selected order was NOT returned: {not_returned:.4f}" , end = "\n\n")

total_deliver = int(input("Enter total number of delivery partners: "))
delyed = int(input("Enter number of delayed partners: "))

on_time_prob = total_deliver - delyed
prob_of_first = on_time_prob / total_deliver
prob_of_second = (on_time_prob - 1) / (total_deliver - 1)
prob_of_both = prob_of_first * prob_of_second

print(f"Probability both randomly chosen partners are on time: {prob_of_both:.4f}" , end = "\n\n")

discount = float(input("Enter probability of a product getting a discount (0 to 1): "))
no_of_pro = int(input("Enter number of products chosen: "))
all_discount = discount ** no_of_pro
print(f"Probability all {no_of_pro} randomly chosen products get discount: {all_discount:.4f}\n")

day = int(input("Enter total number of days in the period (e.g., 7): "))
delay = int(input("Enter number of days with deals (out of 7): "))
res = delay / day
print(f"Probability of finding a deal on a random day: {res:.4f}")

