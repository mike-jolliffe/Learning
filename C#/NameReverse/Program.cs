using System;

namespace NameReverse
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("What's your name? ");
            var name = Console.ReadLine();

            var nameArray = new char[name.Length];

            for (int i = 0; i < name.Length; i++)
            {
                nameArray[i] = name[i];
            }

            Array.Reverse(nameArray);
            Console.WriteLine(nameArray);

            Console.WriteLine("Your name backwards is -- " + String.Join("", nameArray));

        }
    }
}
