from django.shortcuts import render


def home(request):
	return render(request,'home.html')


def count(request):
	text = request.GET['word']
	count=len(text.split())
	return render(request,'count.html',{'count':count,'text':text})