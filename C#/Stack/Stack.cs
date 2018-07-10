using System;
using System.Collections;
namespace Stack
{
    public class Stack
    {
        private ArrayList _list = new ArrayList();

        public void Push(object obj)
        {
            _list.Add(obj);
        }

        public object Pop()
        {
            if (_list.Count > 0)
            {
                var lastIndex = _list.Count - 1;
                var item = _list[lastIndex];
                _list.RemoveAt(lastIndex);
                return item; 
            }
            else
            {
                throw new IndexOutOfRangeException("No more objects on stack.");
            }
        }

        public void Clear()
        {
            _list.Clear();
        }
    }
}
