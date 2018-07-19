using System;
namespace Extensibility
{
    public class ConsoleLogger : ILogger
    {
        public void LogError(string message)
        {
            Log(message, "ERROR");
        }

        public void LogInfo(string message)
        {
            Log(message, "INFO");
        }

        public void Log(string message, string messageType)
        {
            Console.WriteLine(messageType + ": " + message);
        }
    }
}
