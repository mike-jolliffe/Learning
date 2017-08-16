package problems;

public class ComparableTester {
	public static void main(String[] args) {
		Rectangle r1 = new Rectangle();
		Circle c1 = new Circle(0,0,Color.GREEN, 16.0F);
		Circle c2 = new Circle(0,0,Color.GRAY, 16.0F);
		
		System.out.println(r1.compareTo(c1));
		System.out.println(r1.compareTo(c2));
		System.out.println(c1.compareTo(c2));
		
	}
}
