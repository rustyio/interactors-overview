# make_lastname_uppercase.py  
 
# In this fictional example, we make it easy for a user  
# to convert their last name to all uppercase. 
# (Of course, we charge the user for this convenience.) 
# (And we send out an email confirmation.) 
 
from models import (User, Transaction)
import utils.logger
import services.stripe as stripe 
import services.mailer as mailer 
 
log = utils.logger.Logger(scope="MakeLastnameUppercase") 

MINIMUM_DONATION = 500
 
class DonationTooSmallError(RuntimeError): pass 
class NotAllowedError(RuntimeError): pass 
 
class MakeLastnameUppercase(): 
    def __init__(self, user_id, donation_amount): 
        self.user = User.objects.get(id=user_id) 
        self.donation_amount = donation_amount 
        # Make sure user has permission. 
        if not self.user.can_change_name: 
            raise NotAllowedError("...") 
        # Check if user doesn't have enough credit.   
        if self.donation_amount < MINIMUM_DONATION: 
            raise DonationTooSmallError("...") 
 
    def run(self): 
        # Charge the user.
        stripe.charge(self.donation_amount, self.user.stripe_customer_id)
        Transaction(user=self.user, amount=self.donation_amount).save()

        # Convert last name to uppercase. 
        self.user.last_name = self._to_upper(self.user.last_name)
        self.user.save()
 
        # Send a confirmation email. 
        mailer.send(template="make_lastname_uppercase", self.user) 
        return True

    @classmethod
    def _to_upper(cls, s):
        new_s = s.upper()
        log.debug("From %s to %s", s, new_s) 
        return new_s
