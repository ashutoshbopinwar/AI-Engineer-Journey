import numpy as np

# create a sample sales data array with days and prices

# Days 
days = np.array(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])

# Products
products = np.array(["Laptop","Phone","Headphones","Keyboard","Mouse"])

#  Sales Quantity
sales = np.array([
       [5, 10, 15, 8, 20],
    [7, 12, 18, 10, 25],
    [6, 15, 12, 9, 22],
    [8, 14, 20, 11, 28],
    [10, 18, 25, 15, 35],
    [12, 22, 30, 18, 40],
    [9, 16, 22, 13, 32]
])

#  Product Prices
prices = np.array([
    60000,
    25000,
    2000,
    3000,
    1500
])

print("="*60)
print("        SALES DATA ANALYZER")
print("="*60)

# Total Sales Of Each Product
total_product_sales = np.sum(sales, axis=0)

print("\nTotal Sales By Product : ")
print("-"*60)