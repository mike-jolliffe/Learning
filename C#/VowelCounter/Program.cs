using System;

namespace VowelCounter
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please enter a word: ");
            var input = Console.ReadLine().ToCharArray();

            var vowels = "aeiouAEIOU";
            var counter = 0;

            foreach(var letter in input)
            {
                if (vowels.Contains(letter.ToString()))
                {
                    counter++;
                }
            }

            Console.WriteLine(counter);

        }
    }
}
