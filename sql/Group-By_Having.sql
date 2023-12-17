SELECT AVG(price) AS promedy,SUM(sell) FROM product GROUP BY category ORDER BY promedy DESC
SELECT AVG(price) AS promedy,SUM(sell) FROM product GROUP BY category ORDER BY promedy DESC
SELECT AVG(price) AS promedy FROM product GROUP BY category HAVING promedy > 100
SELECT AVG(price) AS promedy FROM product WHERE product_name IS NOT NULL GROUP BY category HAVING promedy > 100
--SELECT
--WHERE
--GROUP BY
--HAVING
--ORDER BY
--LIMIT