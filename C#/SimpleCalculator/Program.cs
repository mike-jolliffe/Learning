using System;

namespace SimpleCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Get inputs
                var input = new Input("Number1: ");
                var num1 = input.GetInput("num");

                var input2 = new Input("Number2: ");
                var num2 = input2.GetInput("num");

                var input3 = new Input("Operation: ");
                var op = input3.GetInput("op");

                Console.WriteLine("{0} {2} {1}", num1, num2, op);

                // Check inputs valid
                var checker = new Checker(num1, num2, op);
                if (checker.Check())
                {
                    checker.Execute();    
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);
            }
        }
    }
}
