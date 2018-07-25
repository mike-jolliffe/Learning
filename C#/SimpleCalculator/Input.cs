using System;
namespace SimpleCalculator
{
    public class Input
    {
        private readonly string _inputMsg;

        public Input(string inputMsg)
        {
            _inputMsg = inputMsg;
        }

        public string GetInput(string type)
        {
            Console.WriteLine(_inputMsg);
            var input = Console.ReadLine();

            if (type == "num")
            {
                try
                {
                    Int32.Parse(input);
                    return input;
                }
                catch (Exception ex)
                {
                    if (ex is FormatException || ex is ArgumentNullException)
                    {
                        throw new Exception("Input must be a valid integer...");
                    }

                    throw new Exception("Something went wrong.");
                }
            }

            if (type == "op")
            {
                return input.ToLower();      
            }

            throw new ArgumentOutOfRangeException(nameof(input), "Please specify 'num' or 'op' as input type");
        }
    }
}
