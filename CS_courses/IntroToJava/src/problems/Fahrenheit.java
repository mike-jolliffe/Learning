package problems;

public class Fahrenheit {

	public static void main(String[] args) {
		// Write a function that converts Fahrenheit to Celsius
		int fahrenheit = 212;
		float celsius = (float)((fahrenheit - 32) * 5.0 / 9.0);

		System.out.println((int)celsius + " degrees Celsius.");
	}

}
