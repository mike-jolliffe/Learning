using System;
namespace DbConnector
{
    public class OracleConnection : DbConnection
    {
        public OracleConnection(string cnxString) : base(cnxString) { }

        public override void Open()
        {
            Console.WriteLine("Opening Oracle database with connection: {0}", base.ConnectionString); ;
        }

        public override void Close()
        {
            Console.WriteLine("Connection closed.");
        }
    }
}
