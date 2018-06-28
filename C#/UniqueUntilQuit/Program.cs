using System;
using System.Collections.Generic;

namespace UniqueUntilQuit
{
    class Program
    {
        static void Main(string[] args)
        {
            var numbers = new List<int>();

            // Allow user to type numbers until input is "Quit"
            while (true)
            {
                Console.Write("Pick a number or type [Quit]: ");
                var input = Console.ReadLine();
                if (input == "Quit")
                {
                    break;
                }
                else
                {
                    int number;
                    var result = Int32.TryParse(input, out number);
                    if (result && !numbers.Contains(number))
                    {
                        numbers.Add(number);
                    }
                    else if (numbers.Contains(number))
                    {
                        continue;
                    }
                    else
                    {
                        Console.WriteLine("I'm sorry, is that a number?");
                    }
                }
            }

            Console.WriteLine(string.Join(", ", numbers));
        }
    }
}
