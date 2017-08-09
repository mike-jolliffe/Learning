package problems;

public class WhileSquare {

	public static void main(String[] args) {
		// use while loop to compute the square of each element
		int i = 0;
		while (i < 9) {
			int sqrd = i * i;
			int cubed = sqrd * i;
			if (cubed % 2 == 0) {
				System.out.println(cubed);
			}
			
			i++;
		}

	}

}
