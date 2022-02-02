-- Show all second_table records
ELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
