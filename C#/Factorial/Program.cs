using System;

namespace Factorial
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Pick a number: ");
            var fact = Int32.Parse(Console.ReadLine());
            var total = 1;

            for (int i = 1; i <= fact; i++)
            {
                total = total * i;
            }
            Console.WriteLine(fact + "! is " + total);

            var simple_fact = Factorial(fact);
            Console.WriteLine(simple_fact);
        }
    }
}
