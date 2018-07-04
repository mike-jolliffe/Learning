using System;

namespace Point
{
    class Program
    {
        static void Main(string[] args)
        {
            int number;
            var parsed = int.TryParse("abc", out number);
            Console.WriteLine(parsed ? "Successful parse": "Failed parse");
        }

        static void UseParams()
        {
            var calculator = new Calculator();
            Console.WriteLine(calculator.Add(1, 2));
            Console.WriteLine(calculator.Add(2, 3, 4));
        }

        static void UsePoints()
        {
            try
            {
                var point = new Point(10, 20);
                point.Move(new Point(40, 60));
                Console.WriteLine("Point is at x: {0}, y: {1}", point.X, point.Y);

                point.Move(100, 200);
                Console.WriteLine("Point is at x: {0}, y: {1}", point.X, point.Y);
            }
            catch (Exception)
            {
                Console.WriteLine("An unexpected error occurred!");
            }
        }
    }
}
