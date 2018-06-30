using System;

namespace Strings2
{
    class Program
    {
        static void Main(string[] args)
        {
            // String methods
            var fullName = "     Mike Jolliffe    ";
            Console.WriteLine("Trimmed white space: '{0}'", fullName.Trim());
            Console.WriteLine("Upper-cased: '{0}'", fullName.Trim().ToUpper());

            var fullNameSplit = fullName.Trim().Split(" ");
            var firstName = fullNameSplit[0];
            var lastName = fullNameSplit[1];

            Console.WriteLine("first name: {0} -- last name: {1}", firstName, lastName);

            var properFullName = fullName.Replace("Mike", "Michael");
            Console.WriteLine(properFullName);

            // Deal with empty, white space only, nulls
            if (String.IsNullOrWhiteSpace(null))
            {
                Console.WriteLine("Null");
            }

            if (String.IsNullOrWhiteSpace(""))
            {
                Console.WriteLine("Empty");
            }

            if (String.IsNullOrWhiteSpace("       "))
            {
                Console.WriteLine("White space");
            }

            // Convert strings to ints and vice versa
            var age = "25";
            // Age can't be greater than 255, so byte makes sense
            Convert.ToByte(age);

            float price = 29.95f;
            // Format specifier for currency
            Console.WriteLine(price.ToString("C"));
        }
    }
}
