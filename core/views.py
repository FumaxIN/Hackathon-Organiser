from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from .models import Hackathons, Enrollment, Submission
from .serializers import HackahonSerializer, CreateHackahonSerializer, EnrollmentSerializer, myEnrollments, SubmissionSerializer, my_Submissions
from rest_framework.parsers import MultiPartParser, FormParser
from datetime import datetime


class HackathonList(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request, *args, **kwargs):
        hackathons = Hackathons.objects.filter(start__gt=datetime.now()).order_by('start')
        serializer = HackahonSerializer(hackathons, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({"message": "You are not authorized to perform this action."}, status=403)
        serializer = CreateHackahonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status":"New Hackathon posted"})
        else:
            print(serializer.errors)
        return Response(serializer.errors)



class Details_Enrol(APIView):
    def get(self, request, hackathonID, *args, **kwargs):
        try:
            gethackathon = Hackathons.objects.get(pk=hackathonID)
            serializer = HackahonSerializer(gethackathon)
            return Response(serializer.data)
        except:
            return Response({"Status":"Not Found"})

    def post(self, request, hackathonID, *args, **kwargs):
        if request.user.is_authenticated:
            gethackathon = Hackathons.objects.get(pk=hackathonID)
            serializer = EnrollmentSerializer(data=request.data, context={'get_hackathon':gethackathon})
            if serializer.is_valid():
                serializer.save(user=request.user, hackathon=gethackathon)
                return Response({"Status":"Enrolled"})
            else:
                return Response(serializer.errors)


@api_view(['GET'])
def my_enrollments(request):
    enrolled = Enrollment.objects.filter(user=request.user)
    serializer = myEnrollments(enrolled, many=True)
    return Response(serializer.data)




class UserSubmission(APIView):
    def get(self, request, hackathonID, *args, **kwargs):
        try:
            gethackathon = Hackathons.objects.get(pk=hackathonID)
            serializer = HackahonSerializer(gethackathon)
            return Response(serializer.data)
        except:
            return Response({"Status": "Not Found"})

    def post(self, request, hackathonID, *args, **kwargs):
        if request.user.is_authenticated:
            gethackathon = Hackathons.objects.get(pk=hackathonID)
            serializer = SubmissionSerializer(data=request.data, partial=True, context={'get_hackathon':gethackathon, 'request':request})
            if serializer.is_valid():
                serializer.save(user=request.user, hackathon=gethackathon)
                return Response({"Status": "Submitted"})
            else:
                return Response(serializer.errors)

@api_view(['GET'])
def my_submissions(request):
    submission = Submission.objects.filter(user=request.user)
    serializer = my_Submissions(submission, many=True)
    return Response(serializer.data)