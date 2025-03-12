# Write your MySQL query statement belo
SELECT unique_id , name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS eu
USING(id);