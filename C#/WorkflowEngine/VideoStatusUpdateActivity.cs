using System;
namespace WorkflowEngine
{
    public class VideoStatusUpdateActivity : IActivity
    {
        public void Execute()
        {
            Console.WriteLine("Database status changed to 'Processing'");
        }
    }
}
