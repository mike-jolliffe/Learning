package lab1;
import lab1.GetInput;

public class MakeMadlib {

	public static void main(String[] args) {
		String[] madlibs = GetInput.madliblist();
		System.out.println("Job Description: " + madlibs[0] + " Scientist");
		System.out.println("Acme Corp is " + madlibs[1] + "ing and needs a " + madlibs[3] + " scientist good with " + madlibs[4]);
		System.out.println("Please " + madlibs[2] + " quickly so we can find a " + madlibs[5]);
	}
}
