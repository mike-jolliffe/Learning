package problems;

public class AvgRainfall {

	public static void main(String[] args) {
		// Function that returns average rainfall for the week, given daily vals
		float dayOne = 1.2F;
		float dayTwo = 0.3F;
		float dayThree = 0.75F;
		float dayFour = 0.0F;
		float dayFive = 3.2F;
		float daySix = 1.1F;
		float daySev = 0.1F;
		
		float avgRainfall = (dayOne + dayTwo + dayThree + dayFour
				             + dayFive + daySix + daySev) / 7.0F;
		
		System.out.println("Average Rainfall: " + avgRainfall + " inches");
		
	}

}

