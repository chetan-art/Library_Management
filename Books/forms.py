from django.forms import ModelForm
from Books.models import Add_Book_detail
class BookAddForm(ModelForm):# here we are create a model based form
    class Meta:
        model = Add_Book_detail
        fields = ['Name','Author_Name','Publish_date','Price'] # this is the feild which we want to display