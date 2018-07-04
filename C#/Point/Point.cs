using System;
namespace Point
{
    public class Point
    {
        public int Y;
        public int X;

        public Point(int x, int y)
        {
            this.X = x;
            this.Y = y; 
        }

        public void Move(int x, int y)
        {
            this.X = x;
            this.Y = y;
        }

        public void Move(Point newLocation)
        {
            if (newLocation == null)
            {
                throw new ArgumentNullException("newLocation");
            }

            Move(newLocation.X, newLocation.Y);
        }
    }
}
