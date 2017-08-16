package problems;

public class ShapeTester {
	public static void main(String[] args) {
		
		Shape[] shapes = new Shape[3];
		
		shapes[0] = new Rectangle();
		shapes[1] = new Rectangle(1.5F, 5.0F, Color.RED, 2.3F, 6.7F);
		shapes[2] = new Circle();
		
		for (Shape shape : shapes) {
			System.out.println("Area for this shape: " + shape.getArea());
		}
		
		Drawable[] drawn = new Drawable[4];
		
		drawn[0] = new Rectangle();
		drawn[1] = new Rectangle(1.5F, 5.0F, Color.RED, 2.3F, 6.7F);
		drawn[2] = new Circle();
		drawn[3] = new Text("Here's some text");
		
		for (Drawable drawable : drawn) {
			drawable.draw();
		}
	}
}
