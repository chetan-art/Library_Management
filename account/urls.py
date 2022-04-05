from django.urls import path,include
from account.views import Signup,Loginup,LogoutPage,Studentregistration,Student_Login
urlpatterns = [
    path('Signup/', Signup),
    path('Loginup/',Loginup,name = "Loginup/"),
    path('Student_Registration/',Studentregistration),
    path('Student_Login/',Student_Login,name="Student_Login/"),
    path('LogoutPage/',LogoutPage),
]