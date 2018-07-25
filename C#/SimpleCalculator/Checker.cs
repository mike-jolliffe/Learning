using System;
using System.Collections.Generic;
namespace SimpleCalculator
{
    public class Checker
    {
        public int Int1 { get; set; }
        public int Int2 { get; set; }
        private readonly string _num1;
        private readonly string _num2;
        private readonly string _op;

        public Checker(string num1, string num2, string op)
        {
            _num1 = num1;
            _num2 = num2;
            _op = op;
        }

        public bool Check()
        {
            var validOps = new List<string>() {
                "add", "+", 
                "subtract", "-", 
                "multiply", "*", 
                "divide", "/"
            };

            try
            {
                Int1 = Int32.Parse(_num1);
                Int2 = Int32.Parse(_num2);
                if (!validOps.Contains(_op))
                {
                    throw new InvalidOperationException( _op + " is not a valid operator.");
                }

                return true;

            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);
                return false;
            }
        }

        public void Execute()
        {
            
            if (_op == "add" || _op == "+")
            {
                Console.WriteLine(Int1 + Int2);
            }
            else if (_op == "subtract" || _op == "-")
            {
                Console.WriteLine(Int1 - Int2);
            }
            else if (_op == "multiply" || _op == "*")
            {
                Console.WriteLine(Int1 * Int2);
            }
            else
            {
                Console.WriteLine(Int1 / Int2);
            }
        }
    }
}
