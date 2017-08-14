package problems;

public class EmpTest {

	public static void main(String[] args) {
		// Create instance of Employee() class

		Employee emp1 = new Employee("Johnny", "Appleseed");
		
		emp1.setSalary(25000.00);
		emp1.setEmployeeId(1);
		
		Employee emp2 = new Employee();
		
		//emp1.showEmp();
		//emp2.showEmp();
		
		
		System.out.println(emp1.toString());
	}
	
}
