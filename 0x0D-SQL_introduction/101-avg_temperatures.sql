-- average by city
-- order by value
SELECT city, SUM(value) / COUNT(*) avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
