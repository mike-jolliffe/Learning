using System;
namespace AccessModifiers2
{
    public class GoldCustomer : Customer
    {
        public void OfferVoucher()
        {
            this.CalculateRating();    
        }
    }
}
