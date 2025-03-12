# Write your MySQL query statement below
SELECT product_name, year, price
FROM Sales AS s
INNER JOIN Product AS p
USING(product_id);