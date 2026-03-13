# Write your MySQL query statement below
-- SELECT (SELECT salary FROM Employee 
-- ORDER BY salary DESC 
-- LIMIT 1 OFFSET 1 ) as SecondHighestSalary

-- USING IF NULL
-- SELECT IFNULL(
--     (
--         SELECT DISTINCT salary 
--         FROM Employee
--         ORDER BY salary DESC
--         LIMIT 1 OFFSET 1
--     ),NULL) AS SecondHighestSalary;
-- the inner query returns the salary and its ranks 
SELECT IFNULL((SELECT salary FROM (SELECT salary,DENSE_RANK() OVER(ORDER BY salary DESC) as rnk FROM Employee) t WHERE rnk=2 LIMIT 1),NULL) AS SecondHighestSalary