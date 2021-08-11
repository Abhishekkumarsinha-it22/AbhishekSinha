from django.shortcuts import render, redirect
from .models import carrer1, education, skills, abouts, certificate, testimonial
from .form import Testform, Testf
from django.contrib import messages


def test(request):
    if request.method == 'POST':
        form = Testform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Review is get submitted.')
            return redirect('/')

    form = Testform()

    return render(request, 'front/testimonial.html', {'form': form})


def home(request):
    carr = carrer1.objects.all()
    edu = education.objects.all().order_by('-id')
    ski = skills.objects.all()
    abo = abouts.objects.all()
    certif = certificate.objects.all().order_by('-id')
    test = testimonial.objects.all().order_by('-id')

    return render(request, 'front/index.html',
                  {'carr': carr, 'edu': edu, 'ski': ski, 'abo': abo, 'certif': certif, 'test': test})
