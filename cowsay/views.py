from django.shortcuts import render
from cowsay.forms import InputForm
from cowsay.models import Input
import subprocess

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            display_text = subprocess.run(
                ['cowsay'] + data['text'].split(), capture_output=True
            ).stdout.decode()
            Input.objects.create(
                text=data['text'] 
            )
        return render(request, "index.html", {"display_text": display_text, "form": form})

    form = InputForm()
    return render(request, "index.html", {"form": form})

def history(request):
    data = Input.objects.order_by('-id')[:10]
    return render(request, 'history.html', {'data': data})