using System;
using System.Collections.Generic;
using System.Linq;

namespace CheckInputString
{
    class Program
    {
        static void Main(string[] args)
        {
            var intList = new List<int>();
            string[] validNums;

            while (true)
            {
                // Get an array of at least five elements from user
                Console.WriteLine("Give me a list of comma-separated numbers: ");
                var numString = Console.ReadLine();

                string[] numArray = numString.Split(",");

                if (numArray == null || numArray.Length < 5)
                {
                    Console.WriteLine("Invalid List");
                    continue;
                }
                else
                {
                    validNums = numArray;
                    var allNums = true;
                    foreach (var num in validNums)
                    {
                        // Try to convert elements of the array to ints and add to list
                        int number;
                        if (Int32.TryParse(num, out number))
                        {
                            intList.Add(number);
                        }
                        else
                        {
                            Console.WriteLine("Please enter all numbers");
                            allNums = false;
                            break;
                        }
                    }
                    if (allNums)
                    {
                        break; 
                    }
                }
            }

            // Sort the list, return three smallest elements to user
            intList.Sort();
            var smallestThree = intList.Take(3);
            Console.WriteLine(
                "The three smallest numbers are: {0}",
                 string.Join(", ", smallestThree)            
            );
        }
    }
}
