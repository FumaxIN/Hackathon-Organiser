from django.db import models
from django.contrib.auth.models import User, AbstractUser

submission_choices = (
    ("image", "Image"),
    ("file", "File"),
    ("link", "Link"),
)

class Hackathons(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    bg_image = models.FileField(upload_to='bg_img', blank=False, null=True)
    hthon_image = models.FileField(upload_to='ht_img', blank=False, null=True)
    submission_type = models.CharField(max_length=6, choices=submission_choices, default='Link', blank=False)
    start = models.DateTimeField(blank=False, null=True)
    end = models.DateTimeField(blank=False, null=True)
    reward = models.TextField(max_length=30, blank=False)


class Enrollment(models.Model):
    hackathon = models.ForeignKey(Hackathons, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    mail = models.EmailField(blank=True)


class Submission(models.Model):
    hackathon = models.ForeignKey(Hackathons, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_name = models.CharField(max_length=30, blank=False, null=True)
    submission_summary = models.TextField(blank=False, null=True)
    submission_file = models.FileField(blank=True, null=True, upload_to='file_submission')
    submission_image = models.ImageField(blank=True, null=True, upload_to='image_submission')
    submission_link = models.URLField(blank=True, null=True)



