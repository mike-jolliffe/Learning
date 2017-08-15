package problems;

public class VehicleTest {

	public static void main(String[] args) {
		// Test fields and methods for superclass and subclass objects

		Vehicle atv = new Vehicle(45, 3);
		Bicycle bike = new Bicycle(30, 10);
		
		//System.out.println(atv);
		//System.out.println(bike);
		
		Vehicle[] vehicles = new Vehicle[3];
		
		vehicles[0] = new Bicycle(30, 10);
		vehicles[1] = new Bicycle(20, 3);
		vehicles[2] = new Vehicle();
		
		for (Vehicle vehicle : vehicles) {
			System.out.println(vehicle);
		}
	}

}
