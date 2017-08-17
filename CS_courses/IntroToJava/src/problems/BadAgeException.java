package problems;

public class BadAgeException extends Exception {
	
	@Override
	public String getMessage() {
		return "Invalid Age: must be between 0 and 120.";
	}
	
}
