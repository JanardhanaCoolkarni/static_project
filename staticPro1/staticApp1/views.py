from django.shortcuts import render

def fun1(request):
	mn="Aditya"
	fp='Ro-Hit'
	fs='python'
	fa='lion'
	d={'name':mn,'player':fp,'subject':fs,'animal':fa}
	return render(request,"staticApp1/1.html",d)