from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {'variable':"this is send "}
    return  render(request,'index.html',context)
    #return HttpResponse("Hello World",)  
def about(request):
    return  render(request,'About.html', )
    #return HttpResponse("About")
def login(request):
    return  render(request,'login.html', )
    #return HttpResponse("login")
def contact(request):
    return  render(request,'Contact.html', )
    #return HttpResponse("Contact")