using System;
using System.Collections.Generic;

namespace SummarizeText
{
    public class StringUtility
    {
        public static string Summarize(string sentence, int maxLength)
        {

            if (sentence.Length < maxLength)
            {
                return sentence;
            }

            var words = sentence.Split(" ");
            var charcount = 0;
            var summaryWords = new List<string>();
            foreach (var word in words)
            {
                charcount += word.Length + 1;
                summaryWords.Add(word);
                if (charcount >= maxLength)
                {
                    break;
                }
            }

            return string.Join(" ", summaryWords) + " ...";

        } 
    }
}
