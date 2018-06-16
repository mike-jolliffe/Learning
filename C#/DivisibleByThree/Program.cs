using System;

namespace DivisibleByThree
{
    class Program
    {
        static void Main(string[] args)
        {
            var counter = 0;
            for (int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0)
                {
                    counter++;
                }
            }

            Console.WriteLine(counter + " numbers are evenly divisible by 3.");
        }
    }
}
