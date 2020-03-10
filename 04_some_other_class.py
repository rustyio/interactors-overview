import app.models
from interactors.make_lastname_uppercase import (
        MakeLastnameUppercase,
        DonationTooSmallError,
        NotAllowedError)

# ...

class MyView(viewsets.GenericViewSet):

    # ...

    def create(self, request, *args, **kwargs):
        # VIEW LOGIC
        user_id = kwargs.get("user_id")
        donation_amount = kwargs.get("donation_amount")
        # END VIEW LOGIC
        try:
            job = MakeLastnameUppercase(user_id, donation_amount)
            if job.run():
                # Send the response.
                pass
        except app.models.DoesNotExist:
            raise Http404()
        except DonationTooSmallError:
            raise exceptions.ValidationError("...")  
        except NotAllowedError:
            raise exceptions.PermissionDenied("...")  

    # ...
