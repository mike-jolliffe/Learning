package problems;

public abstract class Shape implements Drawable, Comparable<Shape> {
	
	// fields for x, y location and color
	private int x;
	private int y;
	private Color shapeColor;
	
	// constructors
	public Shape() {
		this(0, 0, Color.GREEN);
	}

	public Shape(int x, int y, Color shapeColor) {
		super();
		this.x = x;
		this.y = y;
		this.shapeColor = shapeColor;
	}
	
	// getters and setters
	public int getX() {
		return x;
	}

	public void setX(int x) {
		this.x = x;
	}

	public int getY() {
		return y;
	}

	public void setY(int y) {
		this.y = y;
	}

	public Color getShapeColor() {
		return shapeColor;
	}

	public void setShapeColor(Color shapeColor) {
		this.shapeColor = shapeColor;
	}
	
	// methods
	public abstract float getArea();

	@Override
	public void draw() {
		System.out.println("Object type: Shape" + " x: " + x + " y: " + y);
	}
	
	
	public int compareTo(Shape other) {
		if (this.getArea() > other.getArea()) {
			return 1;
		}
		
		else if (this.getArea() < other.getArea()) {
			return -1;
		}
		
		else {
			return 0;
		}
	}
	
	
	
}
