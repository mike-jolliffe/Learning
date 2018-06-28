using System;
using System.Collections.Generic;

namespace FiveUniqueNumbers
{
    class Program
    {
        static void Main(string[] args)
        {

            // Create list to store numbers
            var numbers = new List<int>();


            while (numbers.Count < 5)
            {
                // Ask user for a number
                Console.Write("Please choose a unique number: ");
                var number = Int32.Parse(Console.ReadLine());


                // If number is unique, store it in a list
                if (!numbers.Contains(number))
                {
                    numbers.Add(number);
                }
                // If number is not unique, re-ask for a new number
                else
                {
                    Console.WriteLine("The number {0} was already chosen", number);
                }
            }

            // Once five unique numbers, sort them and return to user
            numbers.Sort();
            Console.WriteLine(string.Join(", ", numbers)); 
        }
    }
}
