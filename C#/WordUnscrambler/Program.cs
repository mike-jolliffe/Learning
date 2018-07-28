using System;

namespace WordUnscrambler
{
    class Program
    {
        static void Main(string[] args)
        {
            bool continueWordUnscramble = true;
            do
            {
                Console.WriteLine("Please enter the option -- [F] for file or [M] for manual");
                var option = Console.ReadLine() ?? string.Empty;

                switch(option.ToUpper())
                {
                    case "F":
                        Console.Write("enter scrambled words filename: ");
                        ExecuteScrambledFileScenario();
                        break;
                    case "M":
                        Console.WriteLine("Enter scrambled words manually: ");
                        ExecuteScrambledManualScenario();
                        break;
                    default:
                        Console.WriteLine("Option was not recognized");
                        break;
                }

                var continueWordUnscrambleDecision = string.Empty;
                do
                {

                    Console.WriteLine("Do you want to continue? [Y] or [N]");
                    continueWordUnscrambleDecision = (Console.ReadLine() ?? string.Empty);

                } while (
                    !continueWordUnscrambleDecision.Equals("Y", StringComparison.OrdinalIgnoreCase) && 
                    !continueWordUnscrambleDecision.Equals("N", StringComparison.OrdinalIgnoreCase));

                continueWordUnscramble = continueWordUnscrambleDecision.Equals("Y", StringComparison.OrdinalIgnoreCase);

            } while (continueWordUnscramble);
        }

        private static void ExecuteScrambledFileScenario()
        {
        }

        private static void ExecuteScrambledManualScenario()
        {
        }
    }
}
