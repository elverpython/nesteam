from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer



def users_list(request):
    user_lst = User.objects.all()
    serializer = UserSerializer(user_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)
