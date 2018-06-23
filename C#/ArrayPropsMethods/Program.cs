using System;

namespace ArrayPropsMethods
{
    class Program
    {
        static void Main(string[] args)
        {
            var nums = new[] { 6, 7, 9, 14, 2, 9, 3 };

            // Length property
            Console.WriteLine("Array is {0} elements. ", nums.Length);

            // Index of first occurrence of particular value
            var index1 = Array.IndexOf(nums, 9);
            Console.WriteLine(index1);

            // Index of second occurrence 
            Console.WriteLine(Array.IndexOf(nums, 9, index1 + 1));

            // Set particular elements to zero
            Array.Clear(nums, 5, 1);
            Console.WriteLine(String.Join(", ", nums));

            // Copy an array 
            var subArray = new int[3];
            Array.Copy(nums, subArray, 3);
            Console.WriteLine(String.Join(", ", subArray));

            // Sort
            Array.Sort(nums);
            Console.WriteLine(String.Join(", ", nums));

            // Reverse
            Array.Reverse(nums);
            Console.WriteLine(String.Join(", ", nums));

        }
    }
}
