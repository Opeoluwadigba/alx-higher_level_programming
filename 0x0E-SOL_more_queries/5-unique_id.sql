-- Create a table 'unique_id' and set its default int value to 1 and make it unique
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
