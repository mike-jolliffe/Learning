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
                var getEmployees = new DbCommand(sqlConn, "select * from Employees");
                getEmployees.Execute();
                sqlConn.Close();

                var orcConn = new OracleConnection("Oracle conn string");
                orcConn.Open();
                var getOracleEmployees = new DbCommand(orcConn, "Some PL/SQL statement");
                getOracleEmployees.Execute();
                orcConn.Close();
            }
            catch (ArgumentException e)
            {
                Console.WriteLine(e);
            }
        }
    }
}
