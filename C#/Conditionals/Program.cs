using System;

namespace Conditionals
{
    
    class Program
    {
        static void Main(string[] args)
        {
            var hour = 9;

            if (hour > 0 && hour < 12)
            {
                Console.WriteLine("morning");
            }
            else if (hour >= 12 && hour < 18)
            {
                Console.WriteLine("afternoon");
            }
            else
            {
                Console.WriteLine("evening");
            }

            var isGoldCustomer = true;

            //float price;
            //if (isGoldCustomer)
            //{
            //    price = 19.95f;
            //}
            //else
            //{
            //    price = 29.95f;
            //}

            float price = (isGoldCustomer) ? 19.95f : 29.95f;

            Console.WriteLine(price);

            var season = Season.Fall;

            switch (season)
            {
                case Season.Fall:
                    Console.WriteLine("It's a beautiful fall day");
                    break;

                case Season.Summer:
                    Console.WriteLine("Summertime! The livin's easy.");
                    break;

                case Season.Spring:
                    Console.WriteLine("Spring is in the air!");
                    break;

                case Season.Winter:
                    Console.WriteLine("Brrr, it's cold out there.");
                    break;

                default:
                    Console.WriteLine("That ain't a season.");
                    break;
            }
        }
    }
}
