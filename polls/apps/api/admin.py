from .models import Poll
from .models import Question
from .models import Choice
from django.contrib import admin

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Question)
