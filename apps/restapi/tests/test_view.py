from apps.restapi.tests import client,status,TestCase,reverse,json,Profile,ProfileSerializers


class StudentListViewTest(TestCase):
  
    def setUp(self):

        self.test_profile=Profile.objects.create(name='Casper', email="gyan@gyan.com", number=798874654, city='Black')
        

    def test_url_exists(self):
        response = self.client.get("/testing")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('testing_get'))
        self.assertEqual(response.status_code, 200)

    # def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('testing_get'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'testing/student_list.html')

    def test_pagination_is_correct(self):
        response = self.client.get(reverse('testing_get'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['student_list']), 10)