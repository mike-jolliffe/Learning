package lab2;
import java.io.Console;

public class PrettyPrintPhone {

	public static void main(String[] args) {
		Console console = System.console();
		
		// Read in phone number from user
		System.out.println("Enter an all-digit phone number: ");
		String phone = console.readLine();
		
		// Make new holder for prettified phone number
		String pretty_phone = "";
		
		for (int i = 0; i < phone.length(); i++){
		    char c = phone.charAt(i);        
		    // Add dashes
		    if (i == 3 || i == 6) {
		    		pretty_phone += "-";
		    		pretty_phone += c;
		    } else {
		    		pretty_phone += c;
		    }
		}
		System.out.println(pretty_phone);
	}
}
