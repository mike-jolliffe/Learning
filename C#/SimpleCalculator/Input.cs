using System;
namespace SimpleCalculator
{
    public class Input
    {
        public double ConvertToNumeric(string argInputText)
        {
            double convertedNumber;
            if (!double.TryParse(argInputText, out convertedNumber))
            {
                throw new ArgumentException("Expected a numeric value.");
            }
            return convertedNumber;
        }
    }
}
