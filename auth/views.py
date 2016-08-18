from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_request(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = LoginForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			post_data = form.cleaned_data
			email = post_data['email']
			password = post_data['password']
			print(email)
			print(password)
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				return redirect('/questions/')
			else:
				return redirect('/failed')
	else:
		form = LoginForm()

	return render(request, 'login.html', {'form': form})

def register(request):
	pass

def failed(request):
	render(request, 'failed.html')