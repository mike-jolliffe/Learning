# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

    def __repr__(self):
        return str(self.id)

class Solution:
    def getImportance(self, employees, root_id):
        """Returns sum of importance for given root employee and all subordinates
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # Create a dictionary of employees
        emp_dict = {e.id: e for e in employees}
        def dfs(eid):
            """Returns total importance for all employees using depth-first search
            :type eid: int
            :rtype: int
            """
            employee = emp_dict[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(root_id)

if __name__ == '__main__':
    boss = Employee(1, 10, [2,3])
    mgr = Employee(2, 8, [4])
    mgr2 = Employee(3, 7, [7])
    underling1 = Employee(4, 4, [])
    underling2 = Employee(7, 4, [])
    workplace = [boss, mgr, mgr2, underling1, underling2]

    sol = Solution()
    print(sol.getImportance(workplace, 1))  # 33
