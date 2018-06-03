using System;

namespace Arrays1
{
    class Program
    {
        static void Main(string[] args)
        {
            var numbers = new int[3];
            numbers[0] = 1;

            Console.WriteLine(numbers[0]);
            Console.WriteLine(numbers[1]);
            Console.WriteLine(numbers[2]);

            var bools = new bool[3];
            bools[0] = true;

            Console.WriteLine(bools[0]);
            Console.WriteLine(bools[1]);
            Console.WriteLine(bools[2]);

            var names = new string[3] { "Mary", "John", "Jack" };
        }
    }
}
