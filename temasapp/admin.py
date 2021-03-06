from django.contrib import admin
from models import Topic, Teacher

"""
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    actions = ['merge_topics']
    
    def merge_topics(self, request, query_set):
        topic = query_set[0]
        print topic
        for obj in query_set[1:]:
            teachers = Teacher.objects.filter(topics=obj.topics)
            for t in teachers:
                t.topics.add(topic)
            obj.delete()
    merge_topics.short_description = "Merge selected topics"
"""
admin.site.register(Topic)
admin.site.register(Teacher)
