from rest_framework.response import Response
from .models import Table, Game
from .serializers import UserSerializer, TableSerializer, GameSerializer, GameSerializer2
from .functions import makeTable
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class Login(APIView):
    permission_classes = ()

    def post(self, request):
      username = request.data.get("username")
      password = request.data.get("password")
      user = authenticate(username=username,password=password)
      if user:
       return Response({"token": user.auth_token.key, "username": user.username, "first_name": user.first_name, "last_name": user.last_name, "email": user.email})
      else:
       return Response({"error": "Credenciales incorrectas"}, status = status.HTTP_400_BAD_REQUEST)

class TableCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = TableSerializer

class TableList(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Table.objects.all()
    serializer_class = TableSerializer

@api_view(['GET'])
def TableDetail(request, pk):
    authentication_classes = ()
    permission_classes = ()
    try:
        table = Table.objects.get(pk=pk)
    except Table.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        table_serializer = TableSerializer(table)
        name = table_serializer.data.get("name")
        words = table_serializer.data.get("words")
        hunts = table_serializer.data.get("hunts")
        return JsonResponse(makeTable(name, words, hunts), safe=False)

@api_view(['GET'])
def UserByToken(request, pk):
    authentication_classes = ()
    permission_classes = ()
    try:
        user = Token.objects.get(key=pk).user
    except Token.DoesNotExist:
        return JsonResponse({'message': 'The token does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({"username": user.username, "id": user.id})


class GameCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = GameSerializer

class GameList(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Game.objects.all().order_by('-time')
    serializer_class = GameSerializer2