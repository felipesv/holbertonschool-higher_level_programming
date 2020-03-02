-- average only 3 citys
-- in specific period
SELECT city, SUM(value) / COUNT(*) avg_temp 
FROM temperatures 
WHERE month >= 7 AND month <= 8
GROUP BY city 
ORDER BY avg_temp DESC
LIMIT 3;
