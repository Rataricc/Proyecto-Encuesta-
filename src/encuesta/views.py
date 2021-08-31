from django.shortcuts import render

def inicio(request):
	return render(request,'index.html')

def principal(request):
	template_name = "principal.html"
	ctx = {
		
	}
	return render(request, template_name, ctx)


