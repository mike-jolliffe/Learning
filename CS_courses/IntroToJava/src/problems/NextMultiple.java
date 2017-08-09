package problems;

public class NextMultiple {

	public static void main(String[] args) {
		// Given two ints--i and j--rounds i to next largest multiple of j
		int i = 256;
		int j = 7; 
		
		int nextMult = i + j - i % j;
		
		System.out.println("Next multiple: " + nextMult);

	}

}
