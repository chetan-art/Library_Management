from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackEnd(ModelBackend):
    def authenticate(self,email, password, **kwargs):
        #print(email)
        UserModel=get_user_model()
       # print(UserModel)
        try:
            user=UserModel.objects.get(email=email)
        #    print(user.email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None