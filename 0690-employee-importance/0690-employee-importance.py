"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {emp.id: emp for emp in employees}

       
        def dfs(emp_id):
            emp = employee_dict[emp_id]
            importance = emp.importance
            for sub_id in emp.subordinates:
                importance += dfs(sub_id)
            return importance

        return dfs(id)