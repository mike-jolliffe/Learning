package problems;

public class UsePerson {
	public static void main(String[] args) {
		Person p = null;
		String name = null;
		int age;
		name = "Some Name"; // comment this line to see InvalidDataException
		age = 15;  // modify age to be < 0 or > 120 to see BadAgeException

		try {
			p = new Person(name, age);
		}
		
		// multi-catch for invalid data or age inputs
		catch (InvalidDataException | BadAgeException e) {
			System.err.println(e.getMessage());
		}

		System.out.println(p);
	}
}
