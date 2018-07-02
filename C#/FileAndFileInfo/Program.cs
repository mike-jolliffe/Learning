using System;
using System.IO;

namespace FileAndFileInfo
{
    class Program
    {
        static void Main(string[] args)
        {
            var path = @"c:\somefile.jpg";

            File.Copy(@"c:\tmp\somefile.jpg", @"d:\tmp\somefile.jpg", true);
            File.Delete(path);
            if (File.Exists(path))
            {
                // Do something
            }
            var content = File.ReadAllText(path);

            var fileInfo = new FileInfo(path);
            fileInfo.CopyTo("...");
            fileInfo.Delete();
            if (fileInfo.Exists)
            {
                // Do something
            }
        }
    }
}
