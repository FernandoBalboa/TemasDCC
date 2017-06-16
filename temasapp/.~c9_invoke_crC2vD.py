from django.test import Client, TestCase

from models import Topic, Teacher
# Create your tests here.


class MergeActionCase(TestCase):

    def setUp(self):
        self.client = Client()
        user = User.objects.create_superuser(
            username='test',
            password='test',
        )
        self.client.force_login(user)
        

    def test(self):
        tema_1 = Topic(name='Sistemas Operativos.')
        tema_2 = Topic(name='S.O.')
        query_set = Topic.objects.all()
        data = { 'action': 'merge', '_selected_action': query_set }
        change_url = self.reverse('admin:merge_topics')
        response = self.post(change_url, data, follow=True)
        self.assertEqual(Topic.object.all().count, 1)
        
        