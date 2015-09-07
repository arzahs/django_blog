from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template 
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def basic_one(request):
	view = "basic_one"
	html = "<html><body>This is %s view</body></html>" % view
	return HttpResponse(html)

def addlike(request, article_id):
	try:
		article = Article.objects.get(id=article_id)
		article.article_likes +=1
		article.save()
	except ObjectDoesNotExist:
		raise Http404
	return redirect("/")

def template_two(request):
	view = "template_two"
	t = get_template('myview.html')
	context = RequestContext(request, {'name': view})
	return HttpResponse(t.render(context))

def template_three(request):
	view = "template_three"
	return render_to_response('myview.html', {'name':view})

def articles(request):
	return render_to_response('articles.html', {'articles': Article.objects.all() })

def article(request, article_id=1):
	return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'comments': Comments.objects.filter(comments_article_id = article_id)})


