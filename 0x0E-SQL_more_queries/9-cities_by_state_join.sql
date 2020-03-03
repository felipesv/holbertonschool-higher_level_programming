--lists all cities contained in the database hbtn_0d_usa.
SELECT b.id, b.name, a.name
FROM cities AS b
JOIN states AS a
ON a.id = b.state_id
ORDER BY b.id ASC;
