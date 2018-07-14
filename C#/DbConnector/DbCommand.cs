using System;
namespace DbConnector
{
    public class DbCommand
    {
        private DbConnection _connection;
        private readonly string _command;

        public DbCommand(DbConnection connection, string command)
        {
            _connection = connection ?? throw new ArgumentNullException(nameof(connection));

            if (String.IsNullOrWhiteSpace(command))
            {
                throw new ArgumentException("Please provide a valid DB command for execution.");
            }

            _command = command;
        }

        public void Execute()
        {
            Console.WriteLine("Executing command: {0}", _command);
        }
    }
}
