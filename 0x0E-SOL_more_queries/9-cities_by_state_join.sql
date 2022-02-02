-- List cities
-- Include states

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
WHERE cities.states_id = states.id
ORDER BY cities.id ASC;
