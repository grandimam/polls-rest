from .models import User
from .models import Poll
from .models import Question
from rest_framework import viewsets
from .serializers import UserSerializer
from .serializers import PollSerializer
from .serializers import QuestionSerializer

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'request': request})
        return Response({"questions": serializer.data})


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'request': request})
        return Response({"polls": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        serializer.save(user=self.request.user)
        return self.create(request, args, kwargs)
