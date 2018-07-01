using System;
using System.Collections.Generic;

namespace DuplicateCheck
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please enter a set of hyphen-separated numbers: ");
            var input = Console.ReadLine();
            var nums = new List<int>();

            if (!String.IsNullOrEmpty(input))
            {
                var inputSplit = input.Split("-");

                foreach (var num in inputSplit)
                {
                    int result;
                    var parsed = Int32.TryParse(num, out result);
                    if (parsed)
                    {
                        nums.Add(result);
                    }
                }
            }

            if (Duplicates(nums))
            {
                Console.WriteLine("Duplicate");
            }
            else
            {
                Console.WriteLine("No Duplicates");
            }

        }

        static bool Duplicates(List<int> nums)
        {
            var numSet = new HashSet<int>(nums);
            // returns true if duplicates
            return nums.Count != numSet.Count;

        }
    }
}
