using System;
using System.Collections.Generic;
using System.Linq;

namespace FormattedConsecutive
{
    class Program
    {
        static void Main(string[] args)
        {
            // Ask for hyphen separated numbers
            Console.WriteLine("Enter hyphen-separated numbers");
            var input = Console.ReadLine();

            var inputSplit = input.Split("-");

            var intList = new List<int>();

            foreach(var num in inputSplit)
            {
                int result;
                var parsed = Int32.TryParse(num, out result);
                if (parsed)
                {
                    intList.Add(result);
                }
            }

            // Check whether those numbers are consecutive
            if (Consecutive(intList))
            {
                Console.WriteLine("Consecutive");
            }
            else
            {
                Console.WriteLine("Not Consecutive");
            }
        }

        static bool Consecutive(List<int> nums)
        {
            // Check if numbers are consecutive
            List<int> sortedList = new List<int>(nums);
            sortedList.Sort();

            // Compares sorted copy to original for equality, order factors in
            return nums.SequenceEqual(sortedList);

        }
    }
}
