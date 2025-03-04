from django.shortcuts import render
from . import forms


# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':#someone hits post request on UI
        form = forms.FormName(request.POST) # create form instance with POST data

        if form.is_valid(): # validate form data
            # DO SOMETHING CODE
            # Process the cleaned data from the form
            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})
