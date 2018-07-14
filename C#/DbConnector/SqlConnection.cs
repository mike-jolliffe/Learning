using System;
namespace DbConnector
{
    public class SqlConnection : DbConnection
    {
        public SqlConnection(string cnxString) : base(cnxString) { }

        public override void Open()
        {
            Console.WriteLine("Opening SQL Server database with connection: {0}", base.ConnectionString);
        }

        public override void Close()
        {
            Console.WriteLine("Connection closed.");
        }
    }
}
