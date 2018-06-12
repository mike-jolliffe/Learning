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

            Console.WriteLine("Pick a width: ");
            var width = Int32.Parse(Console.ReadLine());

            Console.WriteLine("Pick a height: ");
            var height = Int32.Parse(Console.ReadLine());

            var orientation = (width > height) ? "landscape" : "portrait";
            Console.WriteLine("The photo is in " + orientation + " orientation");

        }
    }
}
