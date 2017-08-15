package problems;

public class Rectangle extends Shape {
	// Rectangle fields
	private float width;
	private float height;

	// Rectangle constructors
	public Rectangle() {
		this(0, 0, Color.GREEN, 1, 1);
		
	}

	// Getters and setters for height and width
	public Rectangle(float x, float y, Color shapeColor, float width, float height) {
		super((int)x, (int)y, shapeColor);
		this.width = width;
		this.height = height;
	}

	public float getWidth() {
		return width;
	}

	public void setWidth(int width) {
		this.width = width;
	}

	public float getHeight() {
		return height;
	}

	public void setHeight(int height) {
		this.height = height;
	}

	// Implementation of getArea()
	@Override
	public float getArea() {
		return this.width * this.height; 
		
	}

	
}
