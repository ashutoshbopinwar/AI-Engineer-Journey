import numpy as np

# ---------------------------------
# Inventory Management Analyzer
# ---------------------------------

# creating dataset

# Product names

product = np.array(["Laptop","Phone","Headphones","Keyboard","Mouse","Monitor","Tablet","Webcam"])


# Initial stock available
 
stock = np.array([50,80,100,70,120,60,45,90])


# Units sold

sold = np.array([35,60,72,45,90,40,32,55])


# Price of each product

price = np.array([ 60000,
    25000,
    2000,
    3000,
    1500,
    15000,
    20000,
    4000])


# Minimum stock level before restocking 

reorder_level = np.array([15,20,25,20,30,15,10,20])


# -------------------------------
# Heading
# -------------------------------

print("-" * 65)
print("            INVENTORY MANAGEMENT ANALYZER")
print("-" * 65)

#  calculate remaining stock
remaining_stock = stock - sold


# ---------------------------------------
# Display Inventory
# ---------------------------------------

print("\nINVENTORY DETAILS")
print("-" * 65)

for i in range(len(product)):
    print(
        f"{product[i]:15}  "
        f"Stock : {stock[i]:3}  "
        f"Sold : {sold[i]:3}  "
        f"Remaining : {remaining_stock[i]:3}"
    )
    
    
# ---------------------------------------
# Total Stock Analysis
# ---------------------------------------

total_stock = np.sum(stock)
total_sold = np.sum(sold)
total_remaining = np.sum(remaining_stock)

print("\nSTOCK SUMMARY")
print("-" * 65)

print(f"Total Initial Stock   : {total_stock} units")
print(f"Total Units Sold      : {total_sold} units")
print(f"Total Remaining Stock : {total_remaining} units")


# ---------------------------------------
# Best and Worst Selling Products
# ---------------------------------------

best_selling_index = np.argmax(sold)
least_selling_index = np.argmin(sold)

print("\n SALES PERFORMANCE")
print("-" * 65 )

print(f"Best Selling Product : {product[best_selling_index]}")
print(f"Units Sold           : {sold[best_selling_index]}")

print(f"Least Selling Product : {product[best_selling_index]}")
print(f"Units Sold           : {sold[least_selling_index]}")


# ---------------------------------------
# Lowest Stock Product
# ---------------------------------------

lowest_stock_index = np.argmin(remaining_stock)

print("\nLOWEST STOCK")
print("-" * 65)

print(f"Product : {product[lowest_stock_index]}")
print(f"Remaining Stock : {remaining_stock[lowest_stock_index]} units")


# ---------------------------------------
# Inventory Value
# ---------------------------------------

inventory_value = remaining_stock * price

total_inventory_Value = np.sum(inventory_value)

print("\nINVENTORY VALUE")
print("-" * 65)

for i in range(len(product)):
    print(
        f"{product[i]:15}"
        f"₹{inventory_value[i]:,.2f}"
    )


# ---------------------------------------
# Average Product Price
# ---------------------------------------

average_price = np.mean(price)

print("\nPRICE ANALYSIS")
print("-" * 65)

print(f"Average Product Price : ₹{average_price:,.2f}")
print(f"Highest Product Price : ₹{np.max(price):,.2f}")
print(f"Lowest Product Price : ₹{np.min(price):,.2f}")


# ---------------------------------------
# Restock Analysis
# ---------------------------------------

restock_required = remaining_stock <= reorder_level

print("\nRESTOCK ANALYSIS")
print("-" * 65)

restock_indices = np.where(restock_required)[0]
if len(restock_indices) == 0:
    print("No products need restocking.")
else:
    print("Products that need restocking:")

    for index in restock_indices:
        print(
            f"{product[index]:15} "
            f"Remaining: {remaining_stock[index]:3} "
            f"Required Level: {reorder_level[index]:3}"
        )


# ---------------------------------------
# Stock Remaining Percentage
# ---------------------------------------

stock_percentage = (remaining_stock / stock) * 100

lowest_percentage_index = np.argmin(stock_percentage)

print("\nSTOCK PERCENTAGE")
print("-" * 65)

for i in range(len(product)):
    print(
        f"{product[i]:15} : "
        f"{stock_percentage[i]:.2f}% remaining"
    )

print("-" * 65)

print(
    f"Lowest Remaining Percentage : "
    f"{product[lowest_percentage_index]}"
)

print(
    f"Percentage Remaining        : "
    f"{stock_percentage[lowest_percentage_index]:.2f}%"
)


# ---------------------------------------
# End
# ---------------------------------------

print("\n" + "=" * 65)
print("                    END OF REPORT")
print("=" * 65)