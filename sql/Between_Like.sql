BETWEEN

SELECT * FROM user WHERE id_user BETWEEN 10 AND 30;
SELECT * FROM user WHERE id_user NOT BETWEEN 10 AND 30;
SELECT * FROM user WHERE id_user (BETWEEN 10 AND 30) OR (name="maria");
--SELECT * FROM user WHERE birthdate BETWEEN "1990-01-01" AND "2000-01-01";

LIKE

SELECT * FROM user WHERE name LIKE "mar%";
SELECT * FROM user WHERE name LIKE "%mar%";
SELECT * FROM user WHERE name LIKE "%maria%";

SELECT * FROM user WHERE name LIKE "mar__";
SELECT * FROM user WHERE name LIKE "_ari_";
SELECT * FROM user WHERE name LIKE "mar_%";





