
from apps.restapi.tests import client,status,TestCase,reverse,json,Profile,ProfileSerializers


class UpdateSingleTest(TestCase):
    """ Test module for updating an existing puppy record """

    def setUp(self):
        self.casper = Profile.objects.create(
            name='bakurs', email='xyz@xyx.com', number=1111111, city='white')
        self.muffin = Profile.objects.create(
            name='Muffy', email='xyz@xyx.com', number=1111111, city='white')
        
        self.valid_payload = {
            'name': 'bakurs',
            'email': 'xyz@xyx.com',
            'number': 1111111,
            'city': 'White'
        }
        self.invalid_payload = {
            'name': '',
            'email': 4,
            'number': 'Pamerion',
            'city': 'White'
        }

    def test_valid_update_puppy(self):
        response = client.put(
            reverse('testing_element', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_puppy(self):
        response = client.put(
            reverse('testing_element', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

   