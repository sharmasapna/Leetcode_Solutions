#184
# Write your MySQL query statement below
# We use partition to group by Department and then order by salary in descending order to get the highesst rank
select Department,Employee,Salary
from
(select Department.Name as `Department`,
        Employee.Name as `Employee`,
        Salary,
        DepartmentId,
        dense_rank() over (partition  by DepartmentId order by Salary desc) as rnk
 from Employee
 join Department on Department.Id = Employee.DepartmentId) a
where a.rnk = 1
