SELECT COUNT(name) AS number_of_names FROM user
SELECT SUM(price) FROM product
SELECT AVG(price) FROM product
SELECT ROUND(price) FROM product
SELECT ROUND(AVG(price),2) FROM product
SELECT MIN(price) FROM product --WHERE price IS NOT NULL
SELECT MAX(price) FROM product
SELECT NOW() 

