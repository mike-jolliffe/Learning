using System;

namespace Iterations
{
    class Program
    {
        static void Main(string[] args)
        {
            // Write evens 
            for (int i = 1; i <= 10; i++)
            {
                if (i % 2 == 0)
                {
                    Console.WriteLine(i);
                }
            }

            for (int i = 10; i >= 1; i--)
            {
                if (i % 2 == 0)
                {
                    Console.WriteLine(i);
                }
            }

            var name = "John Smith";
            foreach (var character in name)
            {
                Console.WriteLine(character);
            }

            var numbers = new int[] { 1, 2, 3, 4 };
            foreach (var number in numbers)
            {
                Console.WriteLine(number);
            }

            int j = 1;
            while (j <= 10)
            {
                if (j % 2 == 0)
                {
                    Console.WriteLine(j);
                }

                j++;
            }

            while (true)
            {
                Console.Write("Type your name: ");
                var name2 = Console.ReadLine();
                if (String.IsNullOrWhiteSpace(name2))
                {
                    break;
                }

                Console.WriteLine("@Echo " + name2);
            }
        }
    }
}
