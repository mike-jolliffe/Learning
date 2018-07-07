using System;

namespace Inheritance
{
    public class Text : PresentationObject
    {
        public int FontSize { get; set; }
        public int FontName { get; set; }

        public void AddHyperlink(string url)
        {
            Console.WriteLine("Link to " + url + "added.");
        }
    }
}
