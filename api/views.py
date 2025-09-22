from rest_framework.views import APIView
from rest_framework.response import Response
from .controller import get_model_predictions
class ModelPools(APIView):
    def post(self, request, *args, **kwargs):
        return Response(get_model_predictions(request.data))