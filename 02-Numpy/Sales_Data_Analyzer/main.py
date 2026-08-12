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

for i in range(len(products)):
    print(f"{products[i]:15} : {total_product_sales[i]} units sold")
    
# Best Selling Product :
best_selling_index = np.argmax(total_product_sales)

print("\nBEST SELLING PRODUCT : ")
print("-"*40)
print(f"product:{products[best_selling_index]}")
print(f"Units Sold : {total_product_sales[best_selling_index]}")

# Calculate Revenue
revenue = sales * prices

# Total Revenue 
total_revenue = np.sum(revenue)

print("\nTOTAL REVENUE : ")
print("-"*40)
print(f"{total_revenue:,.2f}")

# Daily Revenue
daily_revenue = np.sum(revenue,axis=1)

print("\n DAILY REVENUE")
print("-"*40)

for i in range(len(days)):
    print(f"{days[i]:12} : ₹{daily_revenue[i]:,.2f}")
    

# Best Sales Day 
best_sales_day_index = np.argmax(daily_revenue)

print("\n BEST SALES DAY")
print("-"*40)
print(f"Day   : {days[best_sales_day_index]}")
print(f"Revenue   : {daily_revenue[best_sales_day_index]:,.2f}")

# Average daily revenue
average_revenue = np.mean(daily_revenue)

print("\nAVERAGE DAILY REVENUE")
print("-" * 40)
print(f"₹{average_revenue:,.2f}")


print("\n" + "=" * 60)
print("                 END OF REPORT")
print("=" * 60)