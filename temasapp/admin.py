from django.contrib import admin
from temasapp.models import Topic, Teacher

class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    actions = ['merge_topics']
    
    def merge_topics(self, request, query_set):
        topic = query_set[0]
        for obj in query_set[1:]:
            teachers = Teacher.objects.filter(topics=obj.pk)
            for t in teachers:
                t.topics.add(topic)
            obj.delete()
    merge_topics.short_description = "Merge selected topics"

admin.site.register(Topic, TopicAdmin)
admin.site.register(Teacher)