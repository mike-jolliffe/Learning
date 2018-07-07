using System;
namespace Stopwatch
{
    public class Stopwatch
    {
        private bool _isRunning = false;
        private DateTime _startTime;
        private DateTime _stopTime;
        private TimeSpan _elapsedTime;

        public Stopwatch()
        {
            _elapsedTime = new TimeSpan();
        }

        public TimeSpan GetTime()
        {
            return _elapsedTime;
        }

        public bool GetStatus()
        {
            return _isRunning;
        }

        public void Start()
        {
            if (_isRunning == false)
            {
                _isRunning = true;
                _startTime = DateTime.Now;
            }
            else
            {
                throw new InvalidOperationException("Cannot start watch twice in a row!");
            }
        }

        public void Stop()
        {
            if (_isRunning == true)
            {
                _isRunning = false;
                _stopTime = DateTime.Now;
                _elapsedTime += (_stopTime - _startTime);

            }
        }
    }
}
