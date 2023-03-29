from django.shortcuts import render, HttpResponse
from django.views import View
import jwt
import datetime
# Create your views here.
JWT_SECRET="secret"
JWT_ALGORITHM="HS256"

def health_check(request):
    return HttpResponse('I am fine')


def encode_jwt(body):
    encoded_jwt = jwt.encode({"user": body['uname'], "exp":datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=60)}, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt
    # >>> print(encoded_jwt)
    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg
    # >>> jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
    # {'some': 'payload'}



class TodoView(View):
    def get(self, request):
        return render(request=request, template_name='form.html')
    
    def post(self, request):
        body_data=request.POST
        
        try:
            decoded =jwt.decode(body_data['jwt'], JWT_SECRET, algorithms=JWT_ALGORITHM)
        except Exception as e:
            return render(request, 'error.html')
        
        print(decoded)
        print(body_data['title'])
        print(body_data['body'])
        return HttpResponse('submitted')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        body_data=request.POST
        jwt=encode_jwt(body_data)
        return HttpResponse(jwt)

        