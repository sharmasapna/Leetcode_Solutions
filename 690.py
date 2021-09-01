#690
"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        # creating a dictionary of the employees based on the employee id
        emp_dict = {}
        for e in employees:
            emp_dict[e.id]= e
        # initialising the resulting importance
        self.res =0

        # recursive function to add the importance of current employee and their subsequent subordinates
        def dfs(empl,id):
            if not empl:
                return
            
            emp = emp_dict[id]
            #print(emp.id)
            self.res += emp.importance
            if not emp.subordinates:
                return
            
            for s in emp.subordinates:
                e = emp_dict[s]
                dfs(e,s)
        dfs(employees,id)
        return self.res
        
            
            
            
