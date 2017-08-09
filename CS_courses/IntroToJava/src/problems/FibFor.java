package problems;

public class FibFor {

	public static void main(String[] args) {
		// compute the first 20 Fibonacci nums with a for loop
		
		// set variables associated with even or odd index
		int fib_run_even = 0;
		int fib_run_odd = 1;
		
		for (int i = 0; i < 19; i++) {
			
			if (i == 0) { 
				System.out.println(i);
			}
			
			else if (i % 2 == 0) {
				fib_run_odd = fib_run_odd + fib_run_even;
				System.out.println(fib_run_odd);
			}
			
			else {
				fib_run_even = fib_run_even + fib_run_odd;
				System.out.println(fib_run_even);
			}
			
		}

	}

}
