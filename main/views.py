from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import QuizModel
from .serializers import QuizSerializer

class QuizView(CreateAPIView):
    queryset = QuizModel.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]