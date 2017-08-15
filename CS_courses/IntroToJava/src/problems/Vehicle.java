package problems;

public class Vehicle {

	// fields
	private int maxSpeed;
	private int numWheels;
	
	// constructors
	public Vehicle() {
		this(60, 4);
	}

	public Vehicle(int maxSpeed, int numWheels) {
		this.maxSpeed = maxSpeed;
		this.numWheels = numWheels;
	}

	// getters and setters
	public int getMaxSpeed() {
		return maxSpeed;
	}

	public void setMaxSpeed(int maxSpeed) {
		this.maxSpeed = maxSpeed;
	}

	public int getNumWheels() {
		return numWheels;
	}

	public void setNumWheels(int numWheels) {
		this.numWheels = numWheels;
	}
	
	// toString method overriding Object() class default
	@Override
	public String toString() {
		return "maxSpeed= " + maxSpeed + ", numWheels= " + numWheels;
	}
	
}
