# Write your MySQL query statement below
-- treat the table as two rows 
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m 
ON e.managerId=m.id
WHERE e.SALARY >m.SALARY;