from django.shortcuts import render
from mysite.forms import ContactForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from books.models import Book
from mysite.models import MyModel
from django.core.mail import send_mail
#from django.http import HttpResponse,Http404
import datetime
def hello(request):
	return HttpResponse("Welcome to the page at %s" %request.get_host())
#        return	display_meta;
def go(request):
	ua = request.META.get('HTTP-USER-AGENT','UNKNOW')
	return HttpResponse("YOUR brower is %s" %ua)
def current_datetime(request):
	current_datetime = datetime.datetime.now()
	return render_to_response('current_datetime.html',locals())
def hours_ahead(request,offset):
	try:
		hours_offset = int(offset)
	except ValueError:
		raise Http404()
	next_time = datetime.datetime.now()+datetime.timedelta(hours=hours_offset)
	return render_to_response("hours_ahead.html",locals())	
def dog(request):
	dog = datetime.datetime.now()
	return render_to_response("dog.html",locals())


def display_meta(request):
	values=request.META.items()
	values.sort()
	html=[]
	for k,v in values:
		html.append('<tr><td>%s</td><td>v</td></tr>' %(k,v))
	return HttpResponse('<table>%s</table>' %'\n'.join(html))	

def display(request):
	values = request.GET
	return render_to_response("display.html",{"values":values})



def search(request):
    errors = []
    if 'q' in request.GET:
	q = request.GET['q']
        if not q:
                errors.append('Enter a search term.')
	elif len(q)>20:
		errors.append('Please enter at most 20 characters.')
        else:
		books = Book.objects.filter(authors__icontains=q)
		return render(request,'search_result.html',{'books':books,'query':q})
    return render(request,'search_form.html',{'errors':errors})


def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('hongbayu@163.com'),
                ['hongbayu@163.com'],
            )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(
		initial={'subject':'I love you'}
	)
    return render(request,'contact_form.html',{'form':form})


def success(request):
    return render(request,'thanks.html')

def foo(*args,**kwargs):
    print "Positional arguments are:"
    print args
    print "keyword arguments are:"
    print kwargs
