# Write your MySQL query statement below
-- group by based on the product key from custimers
SELECT customer_id FROM Customer 
GROUP BY customer_id
HAVING COUNT(DISTINCT Product_key) = (SELECT COUNT(*) FROM Product);