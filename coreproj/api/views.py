from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import FormSerializer
from .models import FormData

class FormView(APIView):
    def get(self, request):
        return Response({"message": "GET request received"}, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id=None):
        try:
            # Get the user by ID (must be provided in the request)
            user = FormData.objects.get(id=id)
        except FormData.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Deserialize the data and update the user
        serializer = FormSerializer(user, data=request.data, partial=True)  # `partial=True` allows for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request - delete a user by ID
    def delete(self, request, id=None):
        try:
            # Get the user by ID
            user = FormData.objects.get(id=id)
        except FormData.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Delete the user
        user.delete()
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        
