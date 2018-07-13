using System;

namespace AbstractClasses
{
    class Program
    {
        static void Main(string[] args)
        {
            var circle = new Circle();
            circle.Draw();

            var rect = new Rectangle();
            rect.Draw();
        }
    }
}
