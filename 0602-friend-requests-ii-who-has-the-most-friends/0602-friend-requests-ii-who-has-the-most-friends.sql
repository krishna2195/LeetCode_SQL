# Write your MySQL query statement below
SELECT id, SUM(num) as num
FROM (
    SELECT requester_id AS id, COUNT(requester_id) AS num
    FROM RequestAccepted
    GROUP BY requester_id
    UNION ALL
    SELECT accepter_id, COUNT(accepter_id)
    FROM RequestAccepted
    GROUP BY accepter_id
    ) temp
GROUP BY id
ORDER BY num DESC
LIMIT 1;