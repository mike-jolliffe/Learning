using System;
using System.Collections.Generic;

namespace ListPropsMethods
{
    class Program
    {
        static void Main(string[] args)
        {
            var numbers = new List<int> { 1, 2, 3, 5, 8, 1, 2 };
            numbers.Add(3);

            numbers.AddRange(new int[3] { 5, 8, 1 });
            Console.WriteLine(String.Join(", ", numbers));

            var index1 = numbers.IndexOf(1);
            var index2 = numbers.IndexOf(1, index1 + 1);
            Console.WriteLine(
                "First index for 1: {0}, second index for 1: {1}",
                index1, 
                index2
            );

            Console.WriteLine(numbers.Count);

            // Remove single instance of 1
            numbers.Remove(1);

            // Remove all instances of 1
            for (int i = 0; i < numbers.Count; i++)
            {
                if (numbers[i] == 1)
                {
                    numbers.Remove(numbers[i]);
                }
            }

            Console.WriteLine(string.Join(", ", numbers));
        }
    }
}
