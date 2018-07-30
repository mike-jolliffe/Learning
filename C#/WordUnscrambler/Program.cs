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



        static void Main(string[] args)
        {
            try
            {
                bool continueWordUnscramble = true;
                do
                {
                    Console.WriteLine(Constants.WordLookupMethod);
                    var option = Console.ReadLine() ?? string.Empty;

                    switch (option.ToUpper())
                    {
                        case Constants.File:
                            Console.Write(Constants.ScrambledWordsFileReq);
                            ExecuteScrambledFileScenario();
                            break;
                        case Constants.Manual:
                            Console.WriteLine(Constants.ScrambledWordsManualReq);
                            ExecuteScrambledManualScenario();
                            break;
                        default:
                            Console.WriteLine(Constants.ScrambleWordsOptionNotRecognized);
                            break;
                    }

                    var continueDecision = string.Empty;
                    do
                    {

                        Console.WriteLine(Constants.ContinueProgramCheck);
                        continueDecision = (Console.ReadLine() ?? string.Empty);

                    } while (
                        !continueDecision.Equals(Constants.Yes, StringComparison.OrdinalIgnoreCase) &&
                        !continueDecision.Equals(Constants.No, StringComparison.OrdinalIgnoreCase));

                    continueWordUnscramble = continueDecision.Equals(Constants.Yes, StringComparison.OrdinalIgnoreCase);

                } while (continueWordUnscramble);
            }
            catch (Exception ex)
            {
                Console.WriteLine(Constants.ErrorProgramWillBeTerminated + ex.Message);
            }
        }

        private static void ExecuteScrambledManualScenario()
        {
            var manualInput = Console.ReadLine() ?? string.Empty;
            string[] scrambledWords = manualInput.Split(',');
            DisplayMatchedUnscrambled(scrambledWords);
        }

        private static void ExecuteScrambledFileScenario()
        {
            try 
            {
                var filename = Console.ReadLine() ?? string.Empty;
                string[] scrambledWords = _fileReader.Read(filename);
                DisplayMatchedUnscrambled(scrambledWords);
            }
            catch (Exception ex)
            {
                Console.WriteLine(Constants.ErrorScrambledWordsCannotBeLoaded + ex.Message);
            }

        }

        private static void DisplayMatchedUnscrambled(string[] scrambledWords)
        {
            string[] wordList = _fileReader.Read(Constants.WordListFilename);

            List<MatchedWord> matchedWords = _wordMatcher.Match(scrambledWords, wordList);

            if (matchedWords.Any())
            {
                foreach(var matchedWord in matchedWords)
                {
                    Console.WriteLine(Constants.MatchFound, 
                                      matchedWord.ScrambledWord, 
                                      matchedWord.Word
                                     );
                }
            }
            else
            {
                Console.WriteLine(Constants.MatchNotFound);
            }
        }
    }
}
