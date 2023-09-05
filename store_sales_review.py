"""
Azubi store has products that customers love. Below are the products, prices and the number of customers that purchased products last week.

The owner wants you to do some calculations on the data with these criteria's:

    -calculate the total price average for all products

    -create a new price list that reduces the old prices by $ 5

    -calculate the total revenue generated from the products

    -calculate the average daily revenue generated from the products

    -based on the new prices, which products are less than $ 30
"""
# DATA
products = ["Sankofa Foods", "Jamestown Coffee",
             "Bioko Chocolate", "Blue Skies Ice Cream",
               "Fair Afric Chocolate", "Kawa Moka Coffee",
                 "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# task 1: Average price of product
print(f"average price of products= ${sum(prices)/len(prices): .2f}\n")

# task 2: New price list, ($5 lesser)

new_prices = [x - 5 for x in prices]
print(f"old prices = {prices}\nnew prices ={new_prices}\n")

# Task 3: Total revenue
revenue_per_product = [price * freq for price, freq in zip(prices, last_week)]
print(f"revenue per product = {revenue_per_product}")
total_revenue = sum(revenue_per_product)
print(f"Total revenue = {total_revenue}\n")

# Task 4: average daily revenue (data was for a week)

av_daily_revenue = total_revenue / 7
print(f"Average daily revenue = {av_daily_revenue}\n")

# Task 5: Products less than $30 from new price list

products_under_30 = [product for product, price in zip(products, new_prices) if price < 30]
print(f"list of products under $30\n {products_under_30} ")