SELECT * FROM user WHERE age = 1 OR age = 2 OR age = 3 OR age = 4 OR age = 5

SELECT * FROM user WHERE age IN (1,2,3,4,5)
SELECT * FROM user WHERE age IN (1,2,3,4,5,6,7,8,9,10)

SELECT * FROM user WHERE age NOT IN (1,2,3,4,5)

SELECT * FROM user WHERE name IN ("maria","juan","pedro")
