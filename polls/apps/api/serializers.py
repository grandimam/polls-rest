from .models import Poll
from .models import Choice
from .models import Question
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import PrimaryKeyRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer


class UserSerializer(ModelSerializer):
    polls = PrimaryKeyRelatedField(queryset=Poll.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'polls']


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

    def __str__(self):
        return self.fields["choice_text"]


class QuestionSerializer(HyperlinkedModelSerializer):
    choices = ChoiceSerializer(source='choice_set', many=True)

    class Meta:
        model = Question
        fields = ['question_text', 'choices']

    def __str__(self):
        return self.fields["question_text"]


class PollSerializer(HyperlinkedModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Poll
        fields = '__all__'
