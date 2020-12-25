from django.shortcuts import render
from form.forms import MyForm

def responseform(request):
    form = MyForm()
    return render(request, 'index_base_layout.html', {'form':form})