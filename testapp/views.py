from django.shortcuts import render
from.import forms

# Create your views here.
def studentinputview(request):
    form=forms.StudentForm()
    my_dict={'form':form}
    return render(request,'testapp/input.html',context=my_dict)
