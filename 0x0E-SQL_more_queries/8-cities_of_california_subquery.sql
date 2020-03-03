-- query with two tables
SELECT b.id, b.name
FROM states AS a, cities AS b
WHERE a.id = b.state_id
	AND a.name = "California";
