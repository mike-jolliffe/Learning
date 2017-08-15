package problems;

public class VehicleTest {

	public static void main(String[] args) {
		// Test fields and methods for superclass and subclass objects

		Vehicle atv = new Vehicle(45, 3);
		Bicycle bike = new Bicycle(30, 10);
		
		System.out.println(atv);
		System.out.println(bike);
	}

}
