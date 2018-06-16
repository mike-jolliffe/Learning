using System;

namespace MaxOfVals
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a group of comma-separated numbers: ");
            var intString = Console.ReadLine();

            string[] nums = intString.Split(",");
            var max = 0;
            foreach (var num in nums)
            {
                if (Int32.Parse(num) > max)
                {
                    max = Int32.Parse(num);
                }
            }

            Console.WriteLine("The max is " + max);
        }
    }
}
