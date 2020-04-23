from django.shortcuts import render
from .models import Article 
from django.http import Http404
# from .article import Article


def index(request):
	postList = Article.objects.all()
	return render(request, 'blog/index.html', {'posts': postList})


def detailsPost(request, id):
	try:
		post = Article.objects.get(pk=id)
	except Article.DoesNotExist:
		raise Http404("Desolé, la publication #{} n'existe pas.".format(id))

	return render(request, 'blog/single.html', {'post': post})

