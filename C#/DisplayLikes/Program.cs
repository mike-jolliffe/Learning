using System;
using System.Collections.Generic;

namespace DisplayLikes
{
    class Program
    {
        static void Main(string[] args)
        {
            var likes = new List<string>();
            string name;

            Console.Write("Enter a name: ");
            name = Console.ReadLine();
            while (!string.IsNullOrEmpty(name))
            {
                likes.Add(name);
                Console.Write("Enter a name: ");
                name = Console.ReadLine();
            }
                
            var arrLength = likes.Count;

            switch (arrLength)
            {
                case 0:
                    Console.WriteLine("Nobody likes your post! Sorry.");
                    break;
                case 1:
                    Console.WriteLine(likes[0] + " likes your post.");
                    break;
                case 2:
                    Console.WriteLine(likes[0] + " and " + likes[1] + " like your post.");
                    break;
                default:
                    string remainder = (arrLength - 2).ToString();
                    Console.WriteLine(
                        likes[0] + ", " + likes[1] + " and " + 
                        remainder + " others like your post.");
                    break;
            }
        }
    }
}
