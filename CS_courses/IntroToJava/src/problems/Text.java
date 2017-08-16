package problems;

public class Text implements Drawable {
	
	// fields
	private String value;

	// constructors
	public Text() {
		this("Empty String");
	}

	public Text(String value) {
		super();
		this.value = value;
	}

	// getters and setters
	public String getValue() {
		return value;
	}

	public void setValue(String value) {
		this.value = value;
	}
	
	// methods
	@Override
	public void draw() {
		System.out.println(value);
	}
}
