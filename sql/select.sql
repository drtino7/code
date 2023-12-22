--select return a table

CREATE TABLE user(
name TEXT,
age INTEGER,
surname TEXT,
id_user INTEGER,
PRIMARY KEY(id_user AUTOINCREMENT)
);

INSERT INTO user(name,age,surname)
VALUES("valentino",16,"grande");

SELECT * FROM user;
SELECT age FROM user;
SELECT age,name FROM user;

--as

SELECT age AS _age_ FROM  user;
SELECT age AS _age_,name AS _name_ FROM  user;

SELECT * FROM user

ORDER BY age ASC
ORDER BY age DESC
ORDER BY NAME ASC
ORDER BY NAME DESC

ORDER BY name,age   --if the same will check age

SELECT * FROM user
ORDER BY age DESC, name ASC;

ORDER BY NAME ASC NULLS LAST
ORDER BY NAME DESC NULLS FIRST

ORDER BY RANDOM()


--DISTINCT

SELECT DISTINCT age FROM user;
SELECT DISTINCT age FROM user ORDER BY age;

--CONCATENATE

SELECT name || "  " || age AS name_age FROM user