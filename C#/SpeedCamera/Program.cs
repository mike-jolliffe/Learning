using System;

namespace SpeedCamera
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please enter a speed limit: ");
            var speedLimit = Int32.Parse(Console.ReadLine());

            Console.WriteLine("Vehicle speed: ");
            var carSpeed = Int32.Parse(Console.ReadLine());

            if (carSpeed < speedLimit)
            {
                Console.WriteLine("OK"); 
            }
            else if (carSpeed - speedLimit >= 60)
            {
                Console.WriteLine("License Suspended");
            }
            else
            {
                var overLimitPoints = (carSpeed - speedLimit) / 5;
                Console.WriteLine(overLimitPoints + " points on license.");
            }
        }
    }
}
