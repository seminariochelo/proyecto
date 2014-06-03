from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
def base(request):
	return render_to_response("base.html",context_instance=RequestContext(request))
# Create your views her.
def registro(request):
	if request.method == "POST":
		formulario=UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario=UserCreationForm()
		return render_to_response("registro.html",{'formulario':formulario},context_instance=RequestContext(request))

	