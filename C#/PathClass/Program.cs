using System;
using System.IO;

namespace PathClass
{
    class Program
    {
        static void Main(string[] args)
        {
            var path = @"C:\Projects\CSharpFundamentals\HelloWorld\HelloWorld.sln";

            Console.WriteLine("Extension: " + Path.GetExtension(path));
            Console.WriteLine("File name: " + Path.GetFileName(path));
            Console.WriteLine("File Name: " + Path.GetFileNameWithoutExtension(path));
            Console.WriteLine("Directory Name: " + Path.GetDirectoryName(path));

        }
    }
}
