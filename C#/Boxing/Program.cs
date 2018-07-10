using System;
using System.Collections;
using System.Collections.Generic;

namespace Boxing
{
    class Program
    {
        static void Main(string[] args)
        {
            // Boxing happens bc passing value type to something that needs object
            var list = new ArrayList();
            list.Add(1);
            list.Add("Mike");
            list.Add(DateTime.Today);

            // No boxing happens, stores int values not object references
            var anotherList = new List<int>();
            anotherList.Add(1);
        }
    }
}
