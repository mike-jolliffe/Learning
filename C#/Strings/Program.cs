using System;

namespace Strings
{
    class Program
    {
        static void Main(string[] args)
        {
            var firstName = "Mike";
            var firstName2 = "Ike";

            var candy = string.Format("{0} and {1}", firstName, firstName2);
            Console.WriteLine(candy);

            var candyNames = new string[3] {"M & Ms", "Skittles", "Nerds"};

            var formattedCandy = string.Join(", ", candyNames);
            Console.WriteLine(formattedCandy);

            var text = "Hey John\nLook into the following paths\nc:\\folder1\\folder2\nc:\\folder3\\folder4";
            Console.WriteLine(text);

            var verbatimText = @"Hey John
Look into the following paths
c:\folder1\folder2
c:\folder3\folder4";
            Console.WriteLine(verbatimText);
        }
    }
}
