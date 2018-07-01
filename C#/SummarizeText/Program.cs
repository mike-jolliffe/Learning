using System;
using System.Collections.Generic;

namespace SummarizeText
{
    class Program
    {
        static void Main(string[] args)
        {
            const int maxLength = 20;
            var sentence = "This is a really really really really long string.";

            Console.WriteLine(StringUtility.Summarize(sentence, maxLength));

        }
    }
}
