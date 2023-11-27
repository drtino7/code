CREATE TABLE user(
age INTEGER,
name TEXT,
surname TEXT,
);

DROP TABLE user;

CREATE TABLE user(
age INTEGER,
name TEXT,
surname TEXT,
id_user INTEGER,
PRIMARY KEY(id_user AUTOINCREMENT)
);

INSERT INTO user(age,name,surname)
VALUES(16,"valentino","grande");