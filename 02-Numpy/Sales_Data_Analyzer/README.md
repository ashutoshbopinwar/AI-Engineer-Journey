# 📊 Sales Data Analyzer

This is my third NumPy project as part of my AI Engineering learning journey.

In this project, I worked with a small sales dataset containing information about different products sold over a week. I used NumPy to calculate total sales, revenue, average revenue, and find the best-performing products and days.

The main goal of this project was to get more comfortable with NumPy arrays and start using them for something closer to real-world data analysis.

## What I Built

The program analyzes sales for these products:

- 💻 Laptop
- 📱 Phone
- 🎧 Headphones
- ⌨️ Keyboard
- 🖱️ Mouse

It can:

- Calculate total units sold for each product
- Find the best-selling product
- Calculate revenue for each product
- Calculate total weekly revenue
- Calculate revenue for each day
- Find the day with the highest revenue
- Calculate average daily revenue

## Dataset

I used sample sales data for 7 days:

| Day | Laptop | Phone | Headphones | Keyboard | Mouse |
|---|---:|---:|---:|---:|---:|
| Monday | 5 | 10 | 15 | 8 | 20 |
| Tuesday | 7 | 12 | 18 | 10 | 25 |
| Wednesday | 6 | 15 | 12 | 9 | 22 |
| Thursday | 8 | 14 | 20 | 11 | 28 |
| Friday | 10 | 18 | 25 | 15 | 35 |
| Saturday | 12 | 22 | 30 | 18 | 40 |
| Sunday | 9 | 16 | 22 | 13 | 32 |

I also added prices for each product and used them to calculate revenue.

## 🛠️ Technologies Used

- Python
- NumPy
- VS Code
- Git & GitHub

## 📚 What I Practiced

This project helped me understand a few NumPy concepts more deeply:

- 2D NumPy arrays
- Indexing
- Array slicing
- `np.sum()`
- `np.mean()`
- `np.argmax()`
- Working with `axis=0`
- Working with `axis=1`
- NumPy broadcasting

One of the most interesting parts for me was this:

```python
revenue = sales * prices


============================================================
             SALES DATA ANALYZER
============================================================

TOTAL SALES BY PRODUCT
----------------------------------------
Laptop          : 57 units
Phone           : 107 units
Headphones      : 142 units
Keyboard        : 84 units
Mouse           : 202 units

BEST SELLING PRODUCT
----------------------------------------
Product : Mouse
Units   : 202

TOTAL REVENUE
----------------------------------------
₹...

DAILY REVENUE
----------------------------------------
Monday       : ₹...
Tuesday      : ₹...
Wednesday    : ₹...
Thursday     : ₹...
Friday       : ₹...
Saturday     : ₹...
Sunday       : ₹...

BEST SALES DAY
----------------------------------------
Day     : ...
Revenue : ₹...

AVERAGE DAILY REVENUE
----------------------------------------
₹...