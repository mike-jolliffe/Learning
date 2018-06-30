using System;

namespace Time
{
    class Program
    {
        static void Main(string[] args)
        {
            // Working with DateTime
            var dateTime = new DateTime(2015, 1, 1);
            var now = DateTime.Now;
            var today = DateTime.Today;

            Console.WriteLine("Current hour: " + now.Hour);
            Console.WriteLine("Current minute: " + now.Minute);

            var tomorrow = now.AddDays(1);
            var yesterday = now.AddDays(-1);
            Console.WriteLine("Tomorrow: " + tomorrow);

            // Format for just current date
            Console.WriteLine(now.ToLongDateString());
            Console.WriteLine(now.ToShortDateString());

            // Format for just current time
            Console.WriteLine(now.ToLongTimeString());
            Console.WriteLine(now.ToShortTimeString());

            // Format for current date and time, default and with format specifiers
            Console.WriteLine(now.ToString());
            Console.WriteLine(now.ToString("yyyy-MM-dd HH:mm"));

            // Working with TimeSpan
            var oneHrTimeSpan = new TimeSpan(1, 0, 0);
            // More readable way, using static method on TimeSpan
            var anotherOneHrTimespan = TimeSpan.FromHours(1);

            // Can also create timespan by operations on multiple DateTime obj
            var start = DateTime.Now;
            var end = DateTime.Now.AddMinutes(2);

            var duration = end - start;
            Console.WriteLine("Duration: " + duration);

            // TimeSpan properties
            var timeSpan = new TimeSpan(1, 30, 30);
            Console.WriteLine(timeSpan);
            Console.WriteLine("Just minutes portion of object: " + timeSpan.Minutes);
            Console.WriteLine("All portions converted to minutes: " + timeSpan.TotalMinutes);

            // TimeSpan methods
            Console.WriteLine("Add one hour: " + timeSpan.Add(TimeSpan.FromMinutes(60)));
            Console.WriteLine("Subtract one hour: " + timeSpan.Subtract(TimeSpan.FromMinutes(60)));

            Console.WriteLine("Parse from string: " + TimeSpan.Parse("01:30:30"));

        }
    }
}
