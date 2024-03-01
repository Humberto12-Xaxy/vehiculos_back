from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

# Create your tests here.

token = Token.objects.get()
client = APIClient()

client.post('api/vehiculos/', {"placas" : "YATZI","longitud" : 15.937423,"latitud" : -93.781098,"user_id" : 1}, format = 'json')
