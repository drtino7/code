SELECT * FROM productcs
SELECT * FROM sales

SELECT product_id ,
sales,
(SELECT name FROM productcs WHERE sal.product_id = product_id)AS name,
(SELECT price FROM productcs WHERE sa.product_id = product_id)AS price
FROM sales AS sal


SELECT product_id,SUM(sales) as total_sales,
(SELECT name FROM products WHERE sales.product_id = product_id) AS name 
(SELECT price FROM sales WHERE sales.product_id = product id) AS price
(total_sales * (SELECT price FROM sales WHERE sales.product_id = product id)) AS total_revenue
FROM sales GROUP BY product_id 
HAVING total_sales > 100
LIMIT 5

SELECT product_id ,
sales,
(SELECT name FROM productcs WHERE sal.product_id = product_id)AS name,
(SELECT price FROM productcs WHERE sa.product_id = product_id)AS price
FROM sales AS sal
WHERE price > 100

--IN CASE THAT WE DONT WANT TO SELECT THE PRICE COLUMN
SELECT product_id ,
sales,
(SELECT name FROM productcs WHERE sal.product_id = product_id)AS name
FROM sales AS sal
WHERE (SELECT price FROM productcs WHERE sal.product_id = product_id) > 100


--CRAETE A VIRTUAL TABLE
SELECT * FROM( SELECT product_id ,
sales,
(SELECT name FROM productcs WHERE sal.product_id = product_id)AS name,
(SELECT price FROM productcs WHERE sal.product_id = product_id)AS price
FROM sales AS sal
WHERE price > 100)