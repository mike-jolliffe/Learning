using System;
namespace WorkflowEngine
{
    public class VideoQueuedNotificationActivity : IActivity
    {
        public void Execute()
        {
            Console.WriteLine("Encoding request sent to web service...");
        }
    }
}
