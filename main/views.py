# from django.shortcuts import render, redirect
# from .models import usser
# from .models import Sitetext
# from .models import ContactRequest
# from .models import ContactRequest2

# def index(request):
#     user=usser.objects.first()

#     text = Sitetext.objects.first()

#     contact = ContactRequest.objects.first()

#     if request.method == "POST":
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         interest = request.POST.get('select')
#         agreed_to_terms = request.POST.get('lterms') == "on"

#         ContactRequest.objects.create(
#             name=name,
#             phone=phone,
#             email=email,
#             interest=interest,
#             agreed_to_terms=agreed_to_terms
#         )

#         return redirect('index')

    
#     contact2 = ContactRequest.objects.first()

#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         agreed_to_terms = request.POST.get('cterms') == "on"

#         ContactRequest2.objects.create(
#             name=name,
#             email=email,
#             message=message, 
#             agreed_to_terms=agreed_to_terms
#         )

#         return redirect('index')
    
#     return render(request, 'main/index.html', {'user':user, 'text':text, 'contact':contact, 'contact2':contact2})

from django.shortcuts import render, redirect
from .models import usser, Sitetext, ContactRequest, ContactRequest2
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    user = usser.objects.first()
    text = Sitetext.objects.first()
    contact = ContactRequest.objects.first()
    contact2 = ContactRequest2.objects.first()  # Սա սխալ էր, ուղղեցի

    if request.method == "POST":
        form_id = request.POST.get('form_id')  # Ստանում ենք, թե որ ձևն է ուղարկվել

        if form_id == "contact1":  # Առաջին ձևի տվյալները
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            interest = request.POST.get('select')
            agreed_to_terms = request.POST.get('lterms') == "on"

            ContactRequest.objects.create(
                name=name,
                phone=phone,
                email=email,
                interest=interest,
                agreed_to_terms=agreed_to_terms
            )
            return redirect('index')

        elif form_id == "contact2":  # Երկրորդ ձևի տվյալները
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            agreed_to_terms = request.POST.get('cterms') == "on"

            ContactRequest2.objects.create(
                name=name,
                email=email,
                message=message, 
                agreed_to_terms=agreed_to_terms
            )
            return redirect('index')

    return render(request, 'main/index.html', {'user': user, 'text': text, 'contact': contact, 'contact2': contact2})
