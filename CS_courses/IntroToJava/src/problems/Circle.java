package problems;

public class Circle extends Shape {
	// circle radius field
	float radius;
	
	// Constructors
	public Circle() {
		this(0,0,Color.GREEN, 1);
	}

	public Circle(int x, int y, Color shapeColor, float radius) {
		super(x, y, shapeColor);
		this.radius = radius;
	}

	// Getters and Setters
	public float getRadius() {
		return radius;
	}

	public void setRadius(float radius) {
		this.radius = radius;
	}

	// Implementation of getArea() method
	@Override
	public float getArea() {
		return (float)(Math.PI * Math.pow(radius, 2.0F));
		
	}

	@Override
	public void draw() {
		System.out.println("Object type: Circle" + ", Radius: " + radius);
	}
	
	
	
}
