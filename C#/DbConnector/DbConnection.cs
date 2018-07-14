using System;
namespace DbConnector
{
    public abstract class DbConnection
    {
        public string ConnectionString { get; set; }
        public TimeSpan Timeout { get; set; }

        public DbConnection(string cnxString)
        {
            if (String.IsNullOrWhiteSpace(cnxString))
            {
                throw new ArgumentException("Please provide a valid DB connection string.");
            }

            ConnectionString = cnxString;
        }

        public abstract void Open();

        public abstract void Close();
    }
}
