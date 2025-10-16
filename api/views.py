from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .serializers import ModelPoolsSerializer
from .controller import get_model_predictions


@permission_classes([AllowAny])
class ModelPoolsView(APIView):
    def post(self, request):
        data = request.data
        serializer = ModelPoolsSerializer(data=data)
        if serializer.is_valid():
            return Response(get_model_predictions(request.data), status=200)
        else:
            return Response(serializer.errors, status=400)
