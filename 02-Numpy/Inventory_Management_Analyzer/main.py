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
    
    