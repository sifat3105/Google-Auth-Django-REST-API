from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def user_detail(request):
    """
    Get the details of the logged-in user.
    """
    user = request.user
    return Response({
        'email': user.email,
        'name': user.get_full_name() or user.username
    })

def google_login_view(request):
    return render(request, 'index.html')

def profile_view(request):
    return render(request, 'profile.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/')
    



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the token to log out
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully."})
