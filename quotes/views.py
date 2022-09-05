
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Quote
from .forms import QuoteForm

# Create your views here.

def index(request):
    
    if request.method=='POST':

        form=QuoteForm(request.POST)
        if form.is_valid():
            quotesub=form.save(commit=False)
            quotesub.user=request.user
            quotesub.save()

            return redirect('index')
    
        else:
            print('formnot sub')
    elif request.method=='GET':
        type=request.GET.get('quotes')
        
        if type=='personal':
            quotespersonal=Quote.objects.filter(user=request.user).order_by('-pk')
            
            context={
               'posts':quotespersonal,
            }
            return render(request, 'quotes/index.html', context=context)
        else:
            quotes=Quote.objects.all().order_by('-pk')
    
            context={
                'posts':quotes,
                }
            return render(request, 'quotes/index.html', context=context)

    form=QuoteForm()

    quotes=Quote.objects.all().order_by('-pk')
    
    context={
        'form':form,
        'posts':quotes,
    }
    return render(request, 'quotes/index.html', context=context)


@login_required
def logout(request):

    django_logout(request)
    domain= settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id= settings.SOCIAL_AUTH_AUTH0_KEY
    return_to='https://naumanquotessh.herokuapp.com'
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

@login_required
def deletequote(request, qoute_id):


    quote=Quote.objects.get(pk=qoute_id)

    quote.delete()

    return redirect('index')

@login_required
def editquote(request, qoute_id):
    quote=Quote.objects.get(pk=qoute_id)

    if request.method=='POST':

        form=QuoteForm(request.POST,instance=quote)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print('form not saved')
    context={
        'quote':quote,
    }

    return render(request, 'quotes/editquote.html',context=context)

