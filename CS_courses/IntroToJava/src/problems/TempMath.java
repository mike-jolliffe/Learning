package problems;

public class TempMath {

	public static void main(String[] args) {
		// Convert Fahrenheit to Celsius and back with two separate methods.
		
		float temp_F = 100F;
		
		// call toCelsius
		float C = toCelsius(temp_F);
		
		// call toFahrenheit
		float F = toFahr(C);
		
		// print a nice, formatted string of results to console
		System.out.println(F + " degrees Fahrenheit is " 
		                   + C + " degrees Celsius.");
		
	}
	
	public static float toCelsius(float temp) {
		// method converting F to C
		return ((temp - 32F) * 5.0F / 9.0F);
	}
	
	public static float toFahr(float temp) {
		// method converting C to F
		return (float)(temp * 9.0F / 5.0F + 32F);
	}
	
	public static String pformat(float C, float F) {
		// method that prints formatted C and F vals to console
		return F + " degrees Fahrenheit is " + C + " degrees Celsius.";
	}

}
