from django.shortcuts import render
from django.http import HttpResponse
from .forms import NoteForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            return HttpResponse("Hello world")
    else:
        form = NoteForm()
    return render(request, 'index.html', {'form':form})
