using System;

namespace Stopwatch
{
    class Program
    {
        static void Main(string[] args)
        {
            var watch = new Stopwatch();
            Console.WriteLine("Welcome to the stopwatch app");
            Console.WriteLine();
            while (true)
            {
                Console.WriteLine(watch.GetStatus() ?
                                  "Press [Enter] to stop the timer!" :
                                  "Press [Enter] to start the timer!");
                var input = Console.ReadLine();
                if (string.IsNullOrEmpty(input))
                {
                    if (watch.GetStatus())
                    {
                        watch.Stop();
                        Console.WriteLine("Elapsed time: {0}", watch.GetTime().ToString(@"s\.ff"));
                    }
                    else
                    {
                        watch.Start();
                        Console.WriteLine("Timer is running...");
                    }
                }
                else 
                {
                    break;
                }
            }
        }
    }
}
