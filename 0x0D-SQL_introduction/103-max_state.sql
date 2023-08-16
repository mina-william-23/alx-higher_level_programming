-- displays the max temperature of each state (ordered by State name).
SELECT state, AVG(value) AS max_temp FROM temperatures ORDER BY state GROUP BY state;
