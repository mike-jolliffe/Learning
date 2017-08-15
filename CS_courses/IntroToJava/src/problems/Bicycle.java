package problems;

public class Bicycle extends Vehicle {

	private int numGears;
	
	public Bicycle() {
		this(25, 10);
	}

	public Bicycle(int maxSpeed, int numGears) {
		super(maxSpeed, 2);
		this.numGears = numGears;
	}

	public int getNumGears() {
		return numGears;
	}

	public void setNumGears(int numGears) {
		this.numGears = numGears;
	}

	@Override
	public String toString() {
		return "numGears= " + numGears + ", " + super.toString();
	}	
	
}
