CREATE TABLE user(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
AGE INTEGER,    
data_born DATATIME
);
CREATE INDEX idx_user_name ON user(name);
CREATE UNIQUE INDEX idx_user_name ON user(name);
CREATE UNIQUE INDEX idx_user_name_lastname ON user(name,lastname);

DROP INDEX idx_user_name;
DROP INDEX idx_user_name_lastname;