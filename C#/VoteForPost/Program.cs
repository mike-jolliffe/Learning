using System;

namespace VoteForPost
{
    class Program
    {
        static void Main(string[] args)
        {
            var post = new Post(
                "First post", 
                "Testing out post voting feature",
                DateTime.Now
            );

            while (true)
            {
                foreach (var kvp in post.GetPost())
                {
                    Console.WriteLine("{0}{1}", kvp.Key, kvp.Value);
                }

                Console.WriteLine("Please upvote with a [+] or downvote with a [-]: ");
                try
                {
                    var vote = Console.ReadLine();
                    post.Vote(vote);
                }
                catch (ArgumentException e)
                {
                    Console.WriteLine(e);
                }
            }
        }
    }
}
