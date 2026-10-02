-- E-commerce Sales Analysis

-- 1. Total revenue
SELECT ROUND(SUM(sales_amount), 2) AS total_revenue
FROM sales;

-- 2. Total quantity sold
SELECT SUM(quantity) AS total_units_sold
FROM sales;

-- 3. Revenue by category
SELECT category,
       ROUND(SUM(sales_amount), 2) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- 4. Monthly revenue
SELECT order_month,
       ROUND(SUM(sales_amount), 2) AS revenue
FROM sales
GROUP BY order_month
ORDER BY order_month;

-- 5. Top products by revenue
SELECT product,
       SUM(quantity) AS units_sold,
       ROUND(SUM(sales_amount), 2) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;

-- 6. Revenue by state
SELECT state,
       ROUND(SUM(sales_amount), 2) AS revenue
FROM sales
GROUP BY state
ORDER BY revenue DESC;

-- 7. Average order value
SELECT ROUND(AVG(sales_amount), 2) AS average_order_value
FROM sales;
