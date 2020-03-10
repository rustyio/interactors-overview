import unittest
import unittest.mock as mock
from interactors import MakeLastnameUppercase
import app.models import User

CLS = MakeLastnameUppercase

class TestMakeLastnameUppercase(unittest.TestCase):
    def setUp(self):
        self.user = User(...)
    
    def test_to_upper(self):
        self.assertEqual(CLS._to_upper('foo'), 'FOO')
        self.assertEqual(CLS._to_upper('Foo'), 'FOO')
    
    def test_not_allowed(self):
        self.user.can_change_name = False
        self.user.save()
        with self.assertRaises(CLS.NotAllowedError) as context:
            CLS(user.id, 600)
        
    def test_donation_too_small(self):
        self.user.save()
        with self.assertRaises(CLS.DonationTooSmallError) as context:
            CLS(self.user.id, 400)
        
    @mock.patch("services.stripe")
    def test_user_gets_charged(self, mock_stripe):
        CLS(self.user.id, 600).run()
        mock_stripe.charge.assert_called_with(600, self.user.stripe_customer_id)

if __name__ == '__main__':
    unittest.main()
