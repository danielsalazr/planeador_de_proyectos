from django.shortcuts import render, redirect
#import for Login
from .form import Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def login_user(request):
    
    message = None

    if request.user.is_authenticated:
        messages.success(request, "Did you forget to log out?")
        return redirect('/reports/')
    else:
        if request.method == "POST":

            print("Se va a iniciar Sesion")

            print(request.POST.get('usuario'))
            print(request.POST.get('contrasenia'))

            form = Login(request.POST)
            if form.is_valid():
                print("Las credenciales son validas")
                username = request.POST['usuario']
                password = request.POST['contrasenia']

                

                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        messages.info(request, "Welcome "+request.user.first_name+", You signed in successfully!")
                        return redirect('/reports/')
                    else:
                        message = "credencial inactiva"
                else:
                    message = "Credenciales erroneas, no existentes o inactivas"
            
        else:
            print("Pero no se inicio")
            form = Login()

        context = {'message': message, 'form':form}
        return render( request, 'login.html', context)
    
@login_required
def logout_user(request):
    logout(request)
    return redirect('/')