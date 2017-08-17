package problems;

public class Person {
    // fields for name and age
	private String name;
    private int age;

    // constructor that throws exceptions for invalid input parameters
    public Person(String n, int a) throws InvalidDataException, BadAgeException {
        if (n == null || n.equals("")) {
            throw new InvalidDataException();
        }
        
        else if (a < 0 || a > 120) {
        		throw new BadAgeException();
        }
        
        name = n;
        age = a;
    }

    // toString method
    public String toString() {
        return "Person [name=" + name + " age=" + age + "]";
    }
}
