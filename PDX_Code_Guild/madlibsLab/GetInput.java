package lab1;
import java.io.Console;


public class GetInput {

	public static String[] madliblist() {
		Console console = System.console();
		if (console == null) {
		    System.out.println("No console: non-interactive mode!");
		    System.exit(0);
		}
		 
		System.out.println("Pick an antonym for data: ");
		String noun1 = console.readLine();
		
		System.out.print("Pick a verb: ");
		String verb1 = console.readLine();
		
		System.out.print("Pick another verb: ");
		String verb2 = console.readLine();

		System.out.println("Pick a sciency adjective: ");
		String adj1 = console.readLine();
		
		System.out.println("Pick an animal: ");
		String noun2 = console.readLine();
		
		System.out.println("Pick a sciency noun: ");
		String noun3 = console.readLine();
		
		return libsToList(noun1, verb1, verb2, adj1, noun2, noun3);
		
	}
	
	public static String[] libsToList(String arg0, String arg1, String arg2, String arg3, String arg4, String arg5) {
		
		String[] madlibs = new String[6];
		
		madlibs[0] = arg0;
		madlibs[1] = arg1;
		madlibs[2] = arg2;
		madlibs[3] = arg3;
		madlibs[4] = arg4;
		madlibs[5] = arg5;
		
		return madlibs;
	}
}
