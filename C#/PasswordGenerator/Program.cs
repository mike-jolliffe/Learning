using System;

namespace PasswordGenerator
{
    class Program
    {
        static void Main(string[] args)
        {
            var random = new Random();

            const int passwordLength = 10;

            var buffer = new char[passwordLength];

            for (var i = 0; i < passwordLength; i++)
                // Generate random lower-case letter from ASCII value
                buffer[i] = (char)('a' + random.Next(0,26));

            var password = new string(buffer);

            Console.WriteLine(password);
        }
    }
}
