CREATE TABLE products (
    id_product INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    price integer
);

INSERT INTO products(product,price)
VALUES("bread",50);
INSERT INTO products(product,price)
VALUES("meat",100);
INSERT INTO products(product,price)
VALUES("chicken",75);
INSERT INTO products(product,price)
VALUES("milk",20);

SELECT * FROM products;


SELECT * FROM products WHERE price < 25;
SELECT * FROM products WHERE price > 50;
SELECT * FROM products WHERE price = 75;
SELECT * FROM products WHERE price >= 75;

SELECT * FROM products WHERE price < 40 ORDER BY PRICE;
SELECT * FROM products WHERE price < 70 ORDER BY id_product;

DELETE FROM products WHERE id_product = 4;

