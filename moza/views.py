from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request,"moza/home.html")

def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			Full_Name = form.cleaned_data['Full_Name']
			Email = form.cleaned_data['Email']
			Phone_No = form.cleaned_data['Phone_No']
			Message = form.cleaned_data['Message']


			Subject = "Response from Contact Form"
			Message = "Name:"+Full_Name+"\n Email:"+Email+"\nPhone_No"+Phone_No+"\nMessage"+Message
			Recipient = ['r4154622@gmail.com']
			sender = 'dharshinirajenderan@gmail.com'

			send_mail(Subject,Message,sender,Recipient) 

	else:	
	    form=ContactForm()
	return render(request,"moza/contact.html",{'form':form})
	


	
	
	

