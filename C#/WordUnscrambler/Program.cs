using System;
using System.Collections.Generic;
using System.Linq;
using WordUnscrambler.Data;
using WordUnscrambler.Workers;

namespace WordUnscrambler
{
    class Program
    {
        private static readonly FileReader _fileReader = new FileReader();
        private static readonly WordMatcher _wordMatcher = new WordMatcher();

        private const string wordListFilename = "wordlist.txt";

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

                var continueDecision = string.Empty;
                do
                {

                    Console.WriteLine("Do you want to continue? [Y] or [N]");
                    continueDecision = (Console.ReadLine() ?? string.Empty);

                } while (
                    !continueDecision.Equals("Y", StringComparison.OrdinalIgnoreCase) && 
                    !continueDecision.Equals("N", StringComparison.OrdinalIgnoreCase));

                continueWordUnscramble = continueDecision.Equals("Y", StringComparison.OrdinalIgnoreCase);

            } while (continueWordUnscramble);
        }

        private static void ExecuteScrambledManualScenario()
        {
            var manualInput = Console.ReadLine() ?? string.Empty;
            string[] scrambledWords = manualInput.Split(',');
            DisplayMatchedUnscrambled(scrambledWords);
        }

        private static void ExecuteScrambledFileScenario()
        {
            var filename = Console.ReadLine() ?? string.Empty;
            string[] scrambledWords = _fileReader.Read(filename);
            DisplayMatchedUnscrambled(scrambledWords);
        }

        private static void DisplayMatchedUnscrambled(string[] scrambledWords)
        {
            string[] wordList = _fileReader.Read(wordListFilename);

            List<MatchedWord> matchedWords = _wordMatcher.Match(scrambledWords, wordList);

            if (matchedWords.Any())
            {
                foreach(var matchedWord in matchedWords)
                {
                    Console.WriteLine("Match found for {0}: {1}", 
                                      matchedWord.ScrambledWord, 
                                      matchedWord.Word
                                     );
                }
            }
            else
            {
                Console.WriteLine("No matches have been found.");
            }
        }
    }
}
