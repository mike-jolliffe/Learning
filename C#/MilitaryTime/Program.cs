using System;

namespace MilitaryTime
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a time in military time format (e.g., 16:30 for 4:30pm): ");
            var input = Console.ReadLine();

            DateTime result;
            var parsed = DateTime.TryParse(input, out result);

            if (parsed)
            {
                Console.WriteLine("Ok");
            }
            else
            {
                Console.WriteLine("Invalid Time");
            }
                                 
        }
    }
}
