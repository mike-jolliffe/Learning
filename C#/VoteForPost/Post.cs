using System;
using System.Collections.Generic;

namespace VoteForPost
{
    public class Post
    {
        private string _Title;
        private string _Description;
        private DateTime _CreatedAt;
        private int _UpVotes = 0;

        public Post(string title, string description, DateTime createdAt)
        {
            this._Title = title;
            this._Description = description;
            this._CreatedAt = createdAt;
        }

        public Dictionary<string, string> GetPost()
        {
            var postDict = new Dictionary<string, string>
            {
                { "Post Title: ", _Title },
                { "Description: ", _Description },
                { "Created: ", _CreatedAt.ToString("MM-dd-yyyy") },
                { "Votes: ", _UpVotes.ToString() }
            };

            return postDict;
        }

        public void Vote(string voteDirection)
        {
            if (voteDirection == "+" )
            {
                _UpVotes++;
            }
            else if (voteDirection == "-")
            {
                _UpVotes--;
            }
            else
            {
                throw new ArgumentException("Voting only accepts a [+] or [-]");
            }
        }
    }
}
