from django.http import HttpRequest
import requests
from django.shortcuts import redirect
from pprint import *
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.

VATSIM_AUTH_URL= 'https://auth-dev.vatsim.net/oauth/authorize?client_id=378&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=full_name+vatsim_details+email+country&required_scopes=full_name+vatsim_details+email+country'
VATSIM_REDIRECT_URI='http://127.0.0.1:8000/oauth2/login/redirect'
VATSIM_CLIENT_ID='378'
VATSIM_CLIENT_SECRET='7eH6w5ec4Zqp2kEbeOfzhbhslmq8VywS6mfSFa05'
VATSIM_SCOPES='full_name vatsim_details email country'



def vatsim_login(request: HttpRequest):
  return redirect(VATSIM_AUTH_URL)

def vatsim_login_redirect(request: HttpRequest):
  code = request.GET.get('code')
  print(code)
  users = exchange_code(code)

  
  request.session['profile'] = users

  try:
      user = User.objects.get(username=users['data']['cid'])

      messages.add_message(request, messages.DEBUG, "User %s already exists, Authenticated? %s" %(user.username, user.is_authenticated))

      login(request,user)

  except:

      user = User.objects.create_user(username=users['data']['cid'], email=users['data']['personal']['email'], first_name=users['data']['personal']['name_first'], last_name=users['data']['personal']['name_last'])

      messages.add_message(request, messages.DEBUG, "User %s is created, Authenticated %s?" %(user.username, user.is_authenticated))

      print("User %s is created, Authenticated %s" %(user.username, user.is_authenticated))

      # remember to log the user into the system
      login(request,user)
  return redirect('http://127.0.0.1:8000/')


def exchange_code(code: str):
  data = {
    "client_id": VATSIM_CLIENT_ID,
    "client_secret": VATSIM_CLIENT_SECRET,
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": VATSIM_REDIRECT_URI,
    "scope": VATSIM_SCOPES
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  response = requests.post("https://auth-dev.vatsim.net/oauth/token", data=data, headers=headers)
  print(response)
  credentials = response.json()
  access_token = credentials['access_token']
  response = requests.get("https://auth-dev.vatsim.net/api/user", headers={
    'Authorization': 'Bearer %s' % access_token,
    'Accept': 'application/json'
  })
  print(response)
  user = response.json()
  print(user)
  return user

def logout(request):
    request.session.flush()
    return redirect('http://127.0.0.1:8000/')
