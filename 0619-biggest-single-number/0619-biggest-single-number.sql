# Write your MySQL query statement below 
SELECT MAX(num) AS num
FROM( SELECT num
FROM Mynumbers
GROUP BY num
HAVING COUNT(*) =1) AS singlenumber;