from django.shortcuts import render
from form.forms import MyForm

def responseform(request):
    form = MyForm()
    return render(request, 'responseform.html', {'form':form})