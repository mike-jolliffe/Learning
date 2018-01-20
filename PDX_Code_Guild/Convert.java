package lab3;
import lab3.MapConversions;
import java.io.Console;
import java.util.*;

public class Convert {

	public static void main(String[] args) {
		// Build conversion maps for converting to meters, and from meters
		HashMap<String, Double> convert_from = MapConversions.toMetersMapper();
		HashMap<String, Double> convert_to = MapConversions.toFinalMapper();
		
		// User input
		Console console = System.console();
		
		// Get magnitude of value
		System.out.println("Gimme the amount: ");
		String s = console.readLine();
		Double value = Double.parseDouble(s);
		
		// Get 'from' units
		System.out.println("What units are you converting from? [km, mi, in, cm, m]: ");
		String from = console.readLine();
		
		// Get 'to' units
		System.out.println("What units are you converting to? [km, mi, in, cm, m]: ");
		String to = console.readLine();
		
		// Grab conversion from the convert_from HashMap
		Double from_val = convert_from.get(from);
		// Multiply given value by from_val
		Double in_meters = value * from_val;
		
		// Convert from meters to final units using convert_to HashMap
		Double to_val = convert_to.get(to);
		// Multiply in_meters value by to_val to get final result
		Double final_val = in_meters * to_val;
		
		System.out.println(s + " " + from + " converts to " + final_val + " " + to + ".");
	}

}
