from django.test import TestCase, Client

# Create your tests here.


class TemasTest(TestCase):
    
    def test_reach_url(self):
        # arrange
        client = Client()
        # act
        response = client.get('/teacher_topics')
        # assert
        self.assertEquals(200,response.status_code)
