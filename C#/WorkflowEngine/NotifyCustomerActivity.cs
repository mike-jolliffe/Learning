using System;
namespace WorkflowEngine
{
    public class NotifyCustomerActivity : IActivity
    {
        public void Execute()
        {
            Console.WriteLine("Encoding status email sent to customer...");
        }
    }
}
