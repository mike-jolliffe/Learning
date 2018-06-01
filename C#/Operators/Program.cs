using System;

namespace Operators
{
    class Program
    {
        static void Main(string[] args)
        {
            var a = 10;
            var b = 3;
            var c = 3;

            Console.WriteLine(a / b);
            Console.WriteLine(c > b && c < a);
        }
    }
}
