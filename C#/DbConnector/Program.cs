using System;

namespace DbConnector
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                var sqlConn = new SqlConnection("SQL conn string");
                sqlConn.Open();
                sqlConn.Close();

                var orcConn = new OracleConnection("Oracle conn string");
                orcConn.Open();
                orcConn.Close();
            }
            catch (ArgumentException e)
            {
                Console.WriteLine(e);
            }
        }
    }
}
