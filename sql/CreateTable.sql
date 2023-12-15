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
INSERT INTO user(age,name,surname)
VALUES(13,"juan","gonzales");
INSERT INTO user(age,name,surname)
VALUES(17,"pedro","perez");
INSERT INTO user(age,name,surname)
VALUES(18,"maria","lopez");
INSERT INTO user(age,name,surname)
VALUES(19,"maria","garcia");
