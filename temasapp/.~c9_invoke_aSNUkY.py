from django.test import TestCase, Client
from django.contrib.auth.models import User
from models import Topic, Teacher
from django.core.urlresolvers import reverse

class MergeActionCase(TestCase):

    def setUp(self):
        self.client = Client()
        user = User.objects.create_superuser('myuser', 'myemail@test.com', 'password')
        self.client.force_login(user)
        

    def test(self):
        tema_1 = Topic(name='Sistemas Operativos.')
        tema_2 = Topic(name='S.O.')
        query_set = Topic.objects.all()
        data = { 'action': 'merge', '_selected_action': query_set }
        change_url = reverse("admin:t")
        response = self.post(change_url, data, follow=True)
        self.assertEqual(Topic.object.all().count, 1)
        
        
class TemasTest(TestCase):
    
    def test_reach_url(self):
        # arrange
        client = Client()
        # act
        response = client.get('/teacher_topics')
        # assert
        self.assertEquals(200,response.status_code)
