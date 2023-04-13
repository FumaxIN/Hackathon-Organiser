from django.contrib import admin
from .models import Hackathons, Enrollment, Submission
from django.contrib import admin

admin.site.register(Hackathons)
admin.site.register(Enrollment)
admin.site.register(Submission)
