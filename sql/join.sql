SELECT * FROM users,job
SELECT * FROM users CROSS JOIN job

SELECT name,lastname FROM user INNER JOIN job ON user.id = job.id

-- id month rewards
-- 2 may 150
-- 7 abril 200
-- 4 november 300
-- 1 may 150
-- 3 abril 200
-- 5 november 300

SELECT name,lastname,reward FROM employees INNER JOIN reward ON employees.id = reward.id

SELECT name,lastname,reward FROM employees LEFT JOIN reward ON employees.id = reward.id
--output: give everthing even if its null

SELECT name,lastname,reward FROM reward LEFT JOIN employees ON employees.id = reward.id
--RIGTH JOIN NO EXIST in sqlite

SELECT name,lastname,reward FROM employees LEFT JOIN reward ON employees.id = reward.id
UNION -- if repits dont show
SELECT name,lastname,reward FROM reward LEFT JOIN employees ON employees.id = reward.id

SELECT name,lastname,reward FROM employees LEFT JOIN reward ON employees.id = reward.id
UNION ALL -- if repits show
SELECT name,lastname,reward FROM reward LEFT JOIN employees ON employees.id = reward.id