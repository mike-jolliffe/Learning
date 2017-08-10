package problems;

public class TempMath {

	public static void main(String[] args) {
		// Convert Fahrenheit to Celsius and back with two separate methods.
		
		float temp_F = 100F;
		
		// call toCelsius and print to console
		float C = toCelsius(temp_F);
		System.out.println(C);
		
		// call toFahrenheit and print to console
		float F = toFahr(C);
		System.out.println(F);
		
	}
	
	public static float toCelsius(float temp) {
		// method converting F to C
		return ((temp - 32F) * 5.0F / 9.0F);
	}
	
	public static float toFahr(float temp) {
		// method converting C to F
		return (float)(temp * 9.0F / 5.0F + 32F);
	}

}
