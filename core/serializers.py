from rest_framework import serializers
from .models import Hackathons, Enrollment, Submission
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone

class HackahonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathons
        fields = '__all__'

class CreateHackahonSerializer(serializers.ModelSerializer):
    bg_image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Hackathons
        fields = '__all__'
    def validate(self, data):
        if data['start'] > data['end']:
            raise ValidationError("start_datetime must be before end_datetime.")
        return data

    def create(self, validated_data):
        instance = Hackathons.objects.create(**validated_data)
        return instance


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['mail']

    def validate(self, data):
        hackathon = self.context.get('get_hackathon')
        enrollment_time = timezone.now()
        if enrollment_time >= hackathon.start:
            raise serializers.ValidationError("Enrollment is only allowed before the start of the Hackathon")
        return data

class myEnrollments(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    # hackathon = serializers.PrimaryKeyRelatedField(queryset=Hackathons.objects.all())
    class Meta:
        model = Submission
        fields = ['submission_name', 'submission_summary', 'submission_file', 'submission_image', 'submission_link']

    def validate(self, data):
        hackathon = self.context.get('get_hackathon')
        submission_type = hackathon.submission_type
        user = self.context['request'].user.id
        # user = data['user']
        enrollment = Enrollment.objects.filter(hackathon=hackathon, user=user).exists()

        if not enrollment:
            raise serializers.ValidationError("User is not enrolled in the Hackathon")
        else:
            if submission_type == 'image' and not data.get('submission_image'):
                raise serializers.ValidationError('Submission type should be image')
            elif submission_type == 'file' and not data.get('submission_file'):
                raise serializers.ValidationError('Submission type should be file')
            elif submission_type == 'link' and not data.get('submission_link'):
                raise serializers.ValidationError('Submission type should be link')

        return data


class my_Submissions(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'