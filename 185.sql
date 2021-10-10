#185
select Department, Employee, Salary
from
    ( select Department.Name as `Department`,
             Employee.Name as `Employee`,
             Salary,
             dense_rank() over (partition by DepartmentId
                                order by Salary desc) as rnk
       from Employee
       join Department on Department.Id = Employee.DepartmentId
     ) a
 where rnk in (1,2,3)
