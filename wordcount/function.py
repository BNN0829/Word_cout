# from django.http import HttpResponse
from django.shortcuts import render


"""def home(request):	
		return HttpResponse('Hello xting')"""

def home(request):
	return render(request,'home.html')


def count(request):
	user_text = request.GET['text']
	length = len(user_text)
	word_dict = {}
	for i in user_text:
		if i not in word_dict:
			word_dict[i] = 1
		else:
			word_dict[i] += 1
	sortedict =\
		sorted(word_dict.items(), key = lambda w:w[1], reverse = True )	

	return render(request,'count.html',{'total':length,
		'word':user_text,'wordict':word_dict,'sortdi':sortedict})


def about(request):
	return render(request,'about.html')
