from rest_framework.serializers import Serializer, CharField
from .models import QuizModel

class QuizSerializer(Serializer):
    name = CharField()
    branch = CharField()
    score = CharField()
    roll_number = CharField()

    def create(self, validated_data):
        return QuizModel.objects.create(**validated_data)