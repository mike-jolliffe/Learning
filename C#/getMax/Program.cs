using System;

namespace getMax
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Pick a first number: ");
            var firstNum = Int32.Parse(Console.ReadLine());

            Console.WriteLine("Pick a second number: ");
            var secondNum = Int32.Parse(Console.ReadLine());

            var max = (firstNum > secondNum) ? firstNum : secondNum;
            Console.WriteLine(max + " is the maximum number.");
        }
    }
}
