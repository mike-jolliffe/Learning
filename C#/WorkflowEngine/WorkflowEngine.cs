using System;
using System.Collections.Generic;

namespace WorkflowEngine
{
    public class WorkflowEngine
    {

        private readonly IList<IActivity> _activities;

        public WorkflowEngine()
        {
            _activities = new List<IActivity>();
        }

        public void Run()
        {
            // Iteratively execute Activities
            foreach (var activity in _activities)
            {
                activity.Execute();
            }

            Console.WriteLine("Workflow finished.");
        }

        public void AddActivity(IActivity activity)
        {
            _activities.Add(activity);
        }
    }
}
