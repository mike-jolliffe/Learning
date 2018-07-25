using System;

namespace SimpleCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                var input = new Input();
                var calculator = new Calculator();

                double firstNumber = input.ConvertToNumeric(Console.ReadLine());
                double secondNumber = input.ConvertToNumeric(Console.ReadLine());
                string operation = Console.ReadLine();

                double result = calculator.Calculate(operation, firstNumber, secondNumber);

                Console.WriteLine(result);

            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
