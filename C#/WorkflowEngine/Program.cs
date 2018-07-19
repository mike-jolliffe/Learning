using System;

namespace WorkflowEngine
{
    class Program
    {
        static void Main(string[] args)
        {
            var engine = new WorkflowEngine();
            engine.AddActivity(new UploadVideoActivity());
            Console.WriteLine("Success");
            engine.AddActivity(new VideoQueuedNotificationActivity());
            engine.AddActivity(new NotifyCustomerActivity());
            engine.AddActivity(new VideoStatusUpdateActivity());
            engine.Run();
        }
    }
}
