
sales = [

 ["Monday", "Shoes", 2, 2500],

 ["Monday", "Shirts", 5, 1200],

 ["Tuesday", "Shoes", 1, 2500],

 ["Tuesday", "Bags", 3, 1800],

 ["Wednesday", "Shirts", 2, 1200],

 ["Wednesday", "Shoes", 4, 2500],

 ["Thursday", "Bags", 1, 1800],

 ["Thursday", "Shirts", 6, 1200],

 ["Friday", "Shoes", 3, 2500],

 ["Friday", "Bags", 4, 1800]

]

product_units = {}

product_revenue = {}

day_revenue = {}

total_revenue = 0

for day, product, quantity, price in sales:

 revenue = quantity * price# Small Business Sales Analysis

This project analyzes weekly sales data using Python.

Concepts used:
- Lists
- Dictionaries
- Loops
- Aggregation
- max(key=...)
- Revenue calculations

Outputs:
- Total revenue
- Product units sold
- Product revenue
- Daily revenue
- Best selling product
- Highest revenue product
- Best revenue day

 total_revenue += revenue

 if product not in product_units:

    product_units[product] = 0

    product_revenue[product] = 0

    product_units[product] += quantity

    product_revenue[product] += revenue

 if day not in day_revenue:

   day_revenue[day] = 0

   day_revenue[day] += revenue

most_units_product = max(product_units, key=product_units.get)

highest_revenue_product = max(product_revenue, key=product_revenue.get)

best_day = max(day_revenue, key=day_revenue.get)

print("Total revenue:", total_revenue)

print("Units sold by product:", product_units)

print("Revenue by product:", product_revenue)

print("Revenue by day:", day_revenue)

print("Most units sold:", most_units_product)

print("Highest revenue:", highest_revenue_product)

print("Best revenue day:", best_day)
