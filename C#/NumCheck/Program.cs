using System;

namespace NumCheck
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number between 1 and 10");
            var input = Int32.Parse(Console.ReadLine());


            if(input > 0 && input < 11)
            {
                Console.WriteLine("VALID");
            }
            else 
            {
                Console.WriteLine("INVALID");
            }

        }
    }
}
