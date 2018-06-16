using System;

namespace Summer
{
    class Program
    {
        static void Main(string[] args)
        {

            var total = 0;

            while (true)
            {
                Console.Write("Please enter a number: ");
                var val = Console.ReadLine();


                if (val == "ok")
                {
                    break;
                }
                else
                {
                    total = total + Int32.Parse(val);  
                }
            }

            Console.WriteLine("The total is " + total);
        }
    }
}
