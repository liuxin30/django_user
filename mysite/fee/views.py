from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Info
from .forms import InfoForm

# Create your views here.
def index(request):
    # return HttpResponse("hello world")
    if request.method == 'POST':
        print(request.POST)
        form = InfoForm(request.POST)
        if form.is_valid():
            fee = form.cleaned_data["fee"]
            return render(request, 'fee/show.html', {'fee': fee})
        message = form.cleaned_data["message"]
    else:
        form = InfoForm()
        message = ''
    return render(request, 'fee/index.html', {'form': form, 'message': message})

