using System;

namespace Variables
{
    class Program
    {
        static void Main(string[] args)
        {
            var number = 5;
            var count = 10;
            var totalPrice = 20.99f;
            var character = 'A';
            var firstName = "Mike";
            var isWorking = true;

            Console.WriteLine(number);
            Console.WriteLine(count);
            Console.WriteLine(totalPrice);
            Console.WriteLine(character);
            Console.WriteLine(firstName);
            Console.WriteLine(isWorking);

            Console.WriteLine("{0} {1}", byte.MinValue, byte.MaxValue);
            Console.WriteLine("{0} {1}", float.MinValue, float.MaxValue);

            const float Pi = 3.14f;
            Console.WriteLine(Pi);
        }
    }
}