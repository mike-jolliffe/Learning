using System;


namespace NumberGuess
{
    class Program
    {
        static void Main(string[] args)
        {
            var rnd = new Random();
            var ans = rnd.Next(1, 10);

            while (true)
            {

                Console.Write("Guess a number between 1 and 10, inclusive: ");
                var guess = Int32.Parse(Console.ReadLine());

                if (guess == ans)
                {
                    Console.WriteLine("You won!");
                    break;
                }
                else
                {
                    Console.WriteLine("Guess again...");
                }
            }
        }
    }
}
