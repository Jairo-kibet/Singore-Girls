from django.urls import path,include
from . import views as v


urlpatterns = [
    path("", v.index, name="home"),
    path("terms/", v.terms, name="terms"),
    path("about/", v.about, name="about"),
    path("services/", v.services, name="services"),
    path("admissions/", v.admissions, name="admissions"),
    path("academics/", v.academics, name="academics"),
    path("facilities/", v.facilities, name="facilities"),
    path("gallery/", v.gallery, name="gallery"),
    path("blog/", v.blog, name="blog"),
    path("contact/", v.contact, name="contact"),
    path("principal/", v.principal, name="principal"),
    path("student_life/", v.student_life, name="student_life"),
    path("cbe/", v.cbe, name="cbe"),
    path("departments/", v.departments, name="departments"),
    path("kcse/", v.kcse, name="kcse")
]