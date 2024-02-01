from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import LetterItemModel
from .forms import AddLetterForm


# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')


def letters_archive(request):
    letters = LetterItemModel.objects.all()

    context = {
        'letters': letters,
    }

    return render(request, 'dashboard/letters_archive.html', context=context)


def add_letter(request):
    if request.method == 'POST':
        form = AddLetterForm(request.POST)
        if form.is_valid():
            AddLetterForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reversed('dashboard:letters_archive'))
    else:
        form = AddLetterForm()

    context = {
        'form': form,
    }

    return render(request, 'dashboard/add_letter.html', context=context)
