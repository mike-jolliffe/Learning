package problems;

public class MonthsArray {

	public static void main(String[] args) {
		// Create an array of the twelve months
		String[] months = {"January", "February", "March", "April",
				           "May", "June", "July", "August", "September",
				           "October", "November", "December"};
		
		String[] months2 = new String[12];
		
		months2[0] = "January";
		months2[1] = "February";
		months2[2] = "March";
		months2[3] = "April";
		months2[4] = "May";
		months2[5] = "June";
		months2[6] = "July";
		months2[7] = "August";
		months2[8] = "September";
		months2[9] = "October";
		months2[10] = "November";
		months2[11] = "December";
		
		
		for (int i = 0; i < months.length; i = i+1) {
			System.out.println(months[i]);
		}
		
		
	}

}

