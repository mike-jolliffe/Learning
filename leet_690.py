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
    def getImportance(self, employees, id):
        """Returns sum of importance for given employee and all subordinates
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        subs_array = []
        emp_importance = None
        # Find starting node
        for employee in employees:
            if employee.id == id:
                for sub in employees:
                    if sub.id in employee.subordinates:
                        subs_array.append(sub)
                emp_importance = employee.importance
                employees.remove(employee)
                break
        return "Employee importance: {} -- Subs: {}".format(emp_importance, subs_array)

if __name__ == '__main__':
    boss = Employee(1, 10, [2,3])
    mgr = Employee(2, 8, [4])
    mgr2 = Employee(3, 7, [7])
    underling1 = Employee(4, 4, [])
    underling2 = Employee(7, 4, [])
    workplace = [boss, mgr, mgr2, underling1, underling2]

    sol = Solution()
    print(sol.getImportance(workplace, 1))  # 33
