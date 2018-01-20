package lab3;
import java.util.*;

public class MapConversions {
	// Create two dictionaries: one for conversion from starting units to meters, another for conversion from meters to final units
	HashMap<String, Double> toVal = new HashMap<String, Double>();
	HashMap<String, Double> fromVal = new HashMap<String, Double>();
	
	public static HashMap<String, Double> toMetersMapper() {
		HashMap<String, Double> fromVal = new HashMap<String, Double>();
		
		// mi to m conversion
		fromVal.put("mi", 1609.34);
		// km to m
		fromVal.put("km", 1000.00);
		// in to m
		fromVal.put("in", 0.0254);
		// cm to m
		fromVal.put("cm", 0.01);
		// m to m
		fromVal.put("m", 1.0);
		
		return fromVal;
	}
	
	public static HashMap<String, Double> toFinalMapper() {
		HashMap<String, Double> toVal = new HashMap<String, Double>();
		
		// m to mi conversion
		toVal.put("mi", 0.0006213);
		// m to km
		toVal.put("km", 0.001);
		// m to in
		toVal.put("in", 39.3701);
		// m to cm
		toVal.put("cm", 100.00);
		// m to m
		toVal.put("m", 1.0);
		
		return toVal;
	}
}
