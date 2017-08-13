package problems;

public class Employee {

	public String firstName;
	public String lastName;
	public double salary;
	public int employeeId;
	public static double minWage = 15.00;
	public static int retirementAge = 65;
	
	public void showEmp() {
		System.out.println(employeeId);
		System.out.println(firstName);
		System.out.println(lastName);
		System.out.println(salary);
		System.out.println(minWage);
		System.out.println(retirementAge);
	}
}
