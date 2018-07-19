using System;
namespace Extensibility
{
    public interface ILogger
    {
        void LogInfo(string message);
        void LogError(string message);
    }
}
