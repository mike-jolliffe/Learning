using System;
namespace Polymorphism
{
    public interface INotificationChannel
    {
        void Send(Message message);
    }
}
