from django.shortcuts import render

# Create your views here.

def logeo(request):
	template_name = "loginvista.html"
	return render(request, template_name)

def registro(request):
	template_name = "registrarvista.html"
	return render(request, template_name)

