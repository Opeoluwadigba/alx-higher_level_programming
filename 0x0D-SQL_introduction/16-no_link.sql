-- Show all second_table records
USE DATABASE hbtn_0c_0;
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
