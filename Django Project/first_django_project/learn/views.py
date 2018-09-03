# coding:utf-8
from django.http import HttpResponse

def index(request):
	return HttpResponse(u"不知道会怎样出现的一行话")