from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

posts = [
    {
        'id':1,
        'content':'Understanding Django Models',
        'paragraph':"Django models are the backbone of any Django project. They provide an abstraction layer to interact with the database and handle data relationships. In this post, we explore how to define models in Django, work with different field types, and how Django's ORM (Object-Relational Mapping) handles queries automatically behind the scenes."
    },
    {
        'id':2,
        'content':'Getting Started with Python OOP',
        'paragraph':"Object-Oriented Programming (OOP) is a powerful programming paradigm in Python that allows developers to structure code in a more modular and reusable way. In this post, we dive into the basic concepts of OOP such as classes, objects, inheritance, and polymorphism. We will walk through how these concepts can help you write cleaner, more maintainable code."


    },
    {
        'id':3,
        'content':'Why You Should Use Flask for Web Development',
        'paragraph':"Flask is a lightweight Python web framework that is perfect for building simple and scalable web applications. In this post, we explain why Flask is a great choice for web development, especially for beginners and small projects. We will also discuss its flexibility and how you can expand it with various extensions for adding more functionality to your apps."
    },
     {
        'id':4,
        'content':'The Future of Artificial Intelligence in Web Development',
        'paragraph':"Artificial Intelligence (AI) is becoming an integral part of web development. From AI-driven chatbots to personalized user experiences, the possibilities are endless. In this post, we explore how AI is transforming web development, including the latest AI tools and libraries that can be integrated into your web apps to improve functionality and user engagement."
    }
]

def home(request):

    return render(request,'posts/home.html',{'posts':posts})

def post(request, id):
    is_valid = False
    for post in posts:
        if post['id'] == id:
            postdict = post
            is_valid = True
            break
    
    
    if is_valid == True:
       
        return render(request,"posts/post.html",{'post':postdict})
    else:
       return HttpResponse("Ohhhhhh Page Notttttt FFFFoundddddddd!!!!!!!!!!")
    

def google(request, id):
    url = reverse("post", args=[id]) 
    print(url)
    return HttpResponseRedirect(url)
