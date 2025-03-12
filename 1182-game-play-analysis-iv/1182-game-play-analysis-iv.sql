# Write your MySQL query statement below
WITH first_login AS(
    SELECT A.player_id, MIN(a.event_date) AS first_login
    FROM Activity A
    GROUP BY A.player_id
), consec_login AS(
    SELECT COUNT(A.player_id) AS num_logins
    FROM first_login f INNER JOIN Activity A
    ON F.player_id = A.player_id
    AND f.first_login = DATE_SUB(A.event_date, INTERVAL 1 DAY)
)
SELECT ROUND(
    (SELECT C.num_logins FROM consec_login C)
    /(SELECT COUNT(F.player_id) FROM first_login F),2)
    AS fraction;