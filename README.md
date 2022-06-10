# VATSIM-oAuth2-Django
An implementation of VATSIM oAuth2 into a Django project. Please note that this is just a Django app that has to be added to an exsisiting project. It is very simple because it uses the default Django user, which is optimal for a small website, but I suggest creating your own user model if the website is for an ARTCC/vACC or above. In VATSIM's oAuth2 settings you have to set `http(s):{yourdomain}/oauth2/login/redirect` as redirect uri.


# How to install
1. Clone or install the repository and add it to the Django Project folder.

2. Add this to your main `settings.py` file, under `INSTALLED_APPS`:
  ```sh
  INSTALLED_APPS = [
    ...
    'VATSIM',
    ...
]
  ```
3. Add this in your main `urls.py` file, under `urlpatterns`: 
```sh
  urlpatterns = [
    ...
    path('', include("VATSIM.urls")),
    ...
]
  ```
  
4. in the VATSIM `views.py` modify the settings with your data:
```sh
VATSIM_AUTH_URL= Eg. 'https://auth.vatsim.net/oauth/authorize?client_id=8&redirect_uri=https%3A%2F%2Fexample.com%2Fconnect%2Fcallback&response_type=code&scope=full_name+vatsim_details+email+country'
VATSIM_REDIRECT_URI=''
VATSIM_CLIENT_ID=''
VATSIM_CLIENT_SECRET=''
VATSIM_SCOPES=''
  ```
5. If not already installed, run:
```sh
pip install requests
  ```

6. You should be pretty much good to go, now when a user logins it creates a user and logs him in. If the user was already created it just logs him in. The user username is the CID.

The current app is meant to be used in the production environment, if you use it in a development one, simply replace every https://auth.vatsim.net with https://auth-dev.vatsim.net, you can read more about this in the developer documentation on VATSIM Github.


If you have any questions/concerns please submit an Issue here.
