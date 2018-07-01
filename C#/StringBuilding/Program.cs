using System;
using System.Text;

namespace StringBuilding
{
    class Program
    {
        static void Main(string[] args)
        {
            var builder = new StringBuilder("Hello World");

            builder
                .Append('!', 3)
                .AppendLine()
                .Append('-', 10)
                .AppendLine()
                .Append("Header")
                .AppendLine();

            builder.Replace('!', '?');

            builder.Remove(15, 10);
            var prepend = "Well ";
            builder.Insert(0, prepend);

            Console.WriteLine(builder);
        }
    }
}
