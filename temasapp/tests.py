from django.test import TestCase, Client
from django.contrib.auth.models import User
from models import Topic, Teacher
from django.core.urlresolvers import reverse

"""
class MergeActionCase(TestCase):

    def setUp(self):
        self.client = Client()
        user = User.objects.create_superuser('myuser', 'myemail@test.com', 'password')
        self.client.force_login(user)
        

    def test(self):
        tema_1 = Topic(name='Sistemas Operativos.')
        tema_2 = Topic(name='S.O.')
        tema_1.save()
        tema_2.save()
        
        query_set = Topic.objects.all()
        data = { 'action': 'merge_topics', '_selected_action': query_set }
        change_url = reverse("admin:temasapp_topic_changelist")
        response = self.client.post(change_url, data, follow=True)
        
        self.assertEqual(Topic.objects.all().count(), 1)
"""        
        
class TemasTest(TestCase):
    
    def test_reach_url(self):
        # arrange
        client = Client()
        # act
        response = client.get('/teacher_topics')
        # assert
        self.assertEquals(200,response.status_code)
