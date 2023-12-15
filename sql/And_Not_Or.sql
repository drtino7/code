SELECT * FROM products WHERE product_id > 50 AND product_id < 55

SELECT * FROM user WHERE name = "maria"
SELECT * FROM user WHERE name = "maria" AND surname = "lopez"
SELECT * FROM user WHERE name = "maria" AND surname = "lopez" AND age > 30

SELECT FROM * user WHERE name = "maria" OR surname = "lopez"
SELECT * FROM user WHERE (name = "maria" AND surname = "lopez") OR (name = "juan" AND AGE < 17)

SELECT * FROM user WHERE NOT age > 20
SELECT * FROM user WHERE NOT age > 20 AND  NOT  name = "maria" ORDER BY RANDOM() LIMIT 2  

