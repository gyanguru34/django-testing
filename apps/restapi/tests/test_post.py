
from apps.restapi.tests import client,status,TestCase,reverse,json

class TestPost(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'email': "abc@abc.com",
            'number': 123456789,
            'city': 'White'
        }
        self.invalid_payload = {
            'name': " ",
            'email': "abcs@abcs.com",
            'number': 123456789,
            'city': 'White'
        }

    def test_create_valid_post(self):
        response = client.post(
            reverse('testing_get'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_post(self):
        response = client.post(
            reverse('testing_get'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

