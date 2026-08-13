# 📦 Inventory Management Analyzer

This is my fourth NumPy project as part of my AI Engineering learning journey.

In this project, I built a simple inventory management system using Python and NumPy.

The idea was to work with something closer to a real business problem instead of just doing basic mathematical calculations.

The program keeps track of products, available stock, units sold, prices and reorder levels. It then uses NumPy to analyze the inventory and find products that need attention.

## What I Built

The program can:

- Show the stock of each product
- Show how many units were sold
- Calculate remaining stock
- Find the total stock
- Find total units sold
- Find the best-selling product
- Find the least-selling product
- Find the product with the lowest remaining stock
- Calculate the value of the remaining inventory
- Calculate the average product price
- Find the highest and lowest product prices
- Find products that need to be restocked
- Calculate the percentage of stock remaining

## Products Used

For this project I used 8 sample products:

- Laptop
- Phone
- Headphones
- Keyboard
- Mouse
- Monitor
- Tablet
- Webcam

## Sample Data

| Product | Stock | Sold | Price | Reorder Level |
|---|---:|---:|---:|---:|
| Laptop | 50 | 35 | ₹60,000 | 15 |
| Phone | 80 | 60 | ₹25,000 | 20 |
| Headphones | 100 | 72 | ₹2,000 | 25 |
| Keyboard | 70 | 45 | ₹3,000 | 20 |
| Mouse | 120 | 90 | ₹1,500 | 30 |
| Monitor | 60 | 40 | ₹15,000 | 15 |
| Tablet | 45 | 32 | ₹20,000 | 10 |
| Webcam | 90 | 55 | ₹4,000 | 20 |

## 🛠️ Technologies Used

- Python
- NumPy
- VS Code
- Git
- GitHub

## 📚 NumPy Concepts I Practiced

This project helped me practice:

- NumPy arrays
- 1D arrays
- Array indexing
- `np.sum()`
- `np.mean()`
- `np.max()`
- `np.min()`
- `np.argmax()`
- `np.argmin()`
- `np.where()`
- Boolean conditions
- Element-wise calculations
- Broadcasting
- Percentage calculations

## One Important Thing I Learned

One of the useful parts of this project was the restock calculation:

```python
restock_required = remaining_stock <= reorder_level