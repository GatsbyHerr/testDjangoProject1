from django.shortcuts import render, HttpResponse, redirect
'''
/- display the string "Hello World" with a method name "index"
'''
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

'''
/new - display the string "There it goes again" with a
method name "new"
'''
def new(request):
    return HttpResponse("There it goes again")

'''
Returning a redirect method and add it next to HTTP
all redirect you will need to always start with a "/"
if you want to move into another method you woule only 
need to add the method (i.e. /example1)

/creat -redirect tp the "/" route with a method call "create"
'''
def create(request):
    return redirect ("/")

'''
lesson: /int:number - display the string
"placeholder of display blog number:{number}" with a method name
"show" (eg. localhost:8000/15 should display the message: 
'placeholder to display blog number 15)
'''
def show(request, number):
    return HttpResponse(f"placeholder of display blog number:{number}")

'''
/int:number/edit -display the string"placeholder to edit blog {number}"
with a method named "edits
'''
def edit(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

'''
/int:number/delete -redirect to the "/" route with a method called "destroy"
'''

def destroy(request, number):
    return redirect("/")