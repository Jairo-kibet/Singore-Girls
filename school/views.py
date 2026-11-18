from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request, "singore/index.html")

def terms(request): 
    return render(request, "singore/terms.html")

def about(request): 
    return render(request, "singore/about.html")

def services(request):
    return render(request, "singore/services.html")

def admissions(request):
    return render(request, "singore/admissions.html")

def academics(request):
    return render(request, "singore/academics.html")

def facilities(request):
    return render(request, "singore/facilities.html")

def gallery(request):
    return render(request, "singore/gallery.html")

def blog(request):
    return render(request, "singore/blog.html")

def contact(request):
    return render(request, "singore/contact.html")

def principal(request):
    return render(request, "singore/principal.html")

def student_life(request):
    return render(request, "singore/student_life.html")

def cbe(request):
    return render(request, "singore/cbe.html")

def departments(request):
    return render(request, "singore/departments.html")

def kcse(request):
    return render(request, "singore/kcse.html")