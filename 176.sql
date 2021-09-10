# 176- SecondHIghestSalary
# Write your MySQL query statement below
SELECT MAX(Salary) as SecondHIghestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee)

# alternate solution
SELECT DISTICT Salary as SecondHighestSalary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
