#184
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
