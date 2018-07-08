using System;
namespace AccessModifiers2
{
    public class Customer
    {
        public int Id { get; set; }
        public string Name { get; set; }

        public void Promote()
        {
            var rating = CalculateRating();
            if (rating == 0)
            {
                Console.WriteLine("Promoted to level 1");
            }
            else
            {
                Console.WriteLine("Promoted to level 2");
            }
        }

        protected int CalculateRating()
        {
            return 0;
        }
    }
}
