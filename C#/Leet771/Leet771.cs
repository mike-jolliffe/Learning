using System;

namespace Leet771
{
    public class Leet771
    {
        public int NumJewelsInStones(string J, string S)
        {
            var jewelCount = 0;
            foreach(var jewel in J)
            {
                foreach(var stone in S)
                {
                    if(jewel == stone)
                    {
                        jewelCount++;
                    }
                }
            }

            return jewelCount;
        }

        public static void Main(string[] args)
        {
            var soln = new Leet771();
            Console.WriteLine("Answer: {0} should be 3", soln.NumJewelsInStones("aA", "aAAbbbb")); 
        }
    }
}

