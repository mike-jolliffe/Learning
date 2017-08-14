package problems;

public class Employee {

	private String firstName;
	private String lastName;
	private double salary;
	private int employeeId;
	
	public Employee(String firstName, String lastName) {
		this.firstName = firstName;
		this.lastName = lastName;
	}

	public Employee() {
		this.firstName = "John";
		this.lastName = "Doe";
	}
	
	public String toString() {
		return "Employee [firstName=" + firstName + ", lastName=" + lastName + ", salary=" + salary + ", employeeId="
				+ employeeId + "]";
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public double getSalary() {
		return salary;
	}

	public void setSalary(double salary) {
		this.salary = salary;
	}

	public int getEmployeeId() {
		return employeeId;
	}

	public void setEmployeeId(int employeeId) {
		this.employeeId = employeeId;
	}

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
