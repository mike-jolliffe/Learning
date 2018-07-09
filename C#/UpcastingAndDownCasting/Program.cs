using System;

namespace UpcastingAndDownCasting
{
    class Program
    {
        static void Main(string[] args)
        {
            Text text = new Text();
            Shape shape = text;

            text.Width = 200;
            shape.Width = 100;

            Console.WriteLine(text.Width);

            Shape shape2 = new Text();
            Text text2 = (Text) shape2;
            text2.FontName = "Courier";
        }
    }
}
