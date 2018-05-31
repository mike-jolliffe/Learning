using System;

namespace TypeConversion
{
    class Program
    {
        static void Main(string[] args)
        {
            byte b = 1;
            int i = b;
            Console.WriteLine(i);

            var number = "1234";
            Convert.ToInt32(number);
            Console.WriteLine(number);

            try
            {
                var num2 = "1234";
                Convert.ToByte(num2);
                Console.WriteLine(num2);
            }
            catch (Exception)
            {
                Console.WriteLine("The number could not be converted to a byte.");
            }

        }
    }
}
