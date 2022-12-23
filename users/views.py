from users.serializers import SignUpSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegisterView(APIView):
    permission_classes = []
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        """
        Возвращает email юзера и 201 статус, если регистрация прошла успешно
        :param request:
        :return:
        """
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'email': serializer.data['email']}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
