using System;
using System.Collections.Generic;

namespace MakePascalVar
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please type a few words separated by spaces: ");
            var input = Console.ReadLine().Split(" ");

            var forPascal = new List<string>();
            foreach(var word in input)
            {

                var firstLetter = word[0].ToString().ToUpper();
                var allLower = word.ToLower();
                var capFirst = char.ToUpper(allLower[0]) + allLower.Substring(1);
                forPascal.Add(capFirst);

            }

            Console.WriteLine(string.Join("", forPascal));

        }
    }
}
