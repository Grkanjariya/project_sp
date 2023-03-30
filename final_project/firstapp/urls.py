from django.urls import path

from . import views

# urlpatterns= [path("",views.signin,name="signin")]
urlpatterns= [path("",views.home_2,name="home_2"),
              path("home",views.home,name="home"),
              path("home_3",views.home_3,name="home_3"),
              path("signin",views.signin,name="signin"),
              path("login",views.login,name="login"),
              path("register",views.register,name="register"),
              path("register_doctor",views.register_doctor,name="register_doctor"),
              path("view_appointment",views.view_appointment,name="view_appointment"),
              path("logout",views.logout,name="logout"),
              path("form",views.form,name="form"),
              path("confirmation",views.confirmation,name="confirmation"),
              path("feedback",views.feedback,name="feedback"),
             ] 
