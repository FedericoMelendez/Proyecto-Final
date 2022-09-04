from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from users.models import User_profile
from users.forms import User_profile_Form
from users.forms import User_registration_form
from django.contrib.auth import login,authenticate,logout

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                context = {'message':f'Bienvenido {username}!! :D'}
                return render(request, 'index.html', context = context)

        form = AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Formulário inválido', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'users/register.html', context)

    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form': form})

def show_profile(request):
    if request.user.is_authenticated:
        return HttpResponse(request.user.profile.phone)

def create_profile(request):#crea el perfil por primera vez
    if request.method=='POST':
        form = User_profile_Form(request.POST, request.FILES)
        if form.is_valid():
            User_profile.objects.create(
                    user = request.user,
                    phone = form.cleaned_data['phone'],
                    name = form.cleaned_data['name'],
                    lastname = form.cleaned_data['lastname'],
                    adress = form.cleaned_data['adress'],
                    profile_image = form.cleaned_data['profile_image'],
            )
            return redirect(login_request)
    elif request.method == 'GET':
            form = User_profile_Form()
            context = {'form':form}
            return render(request,'users/create_profile.html', context=context)



def edit_profile (request, pk): #No pude hacer que funcione - Futuras pruebas. 
    if request.method == 'POST':
        form = User_profile_Form(request.POST, request.FILES)
        if form.is_valid():
            profile = User_profile.objects.get(id=pk)
            profile.phone = form.cleaned_data['phone']
            profile.name = form.cleaned_data['name']
            profile.lastname = form.cleaned_data['lastname']
            profile.adress = form.cleaned_data['adress']
            if form.cleaned_data['profile_image']:
                profile.profile_image=form.cleaned_data['profile_image']
            profile.save()

            return redirect(login_request)


    elif request.method == 'GET':
        profile = User_profile.objects.get(id=pk)

        form = User_profile_Form(initial={
                                        'name':profile.name,
                                        'lastname':profile.lastname,
                                        'adress':profile.adress,
                                        'profile_image':profile.profile_image})
        context = {'form':form}
        return render(request, 'users/edit_profile.html', context=context)