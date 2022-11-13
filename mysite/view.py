# i have created this file - prasanna agnihotri
# view always return a http response

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request,'index.html')

def ex1(request):
    return HttpResponse('''
    <h1>ex1</h1> ''')

def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')

    #checkbos values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')

    #check with checkbox is on or off
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed  = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase','analyzed_text':analyzed}

        return render(request,'analyze.html',params)

    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !=  "\n":
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed New Lines','analyzed_text':analyzed}

        return render(request,'analyze.html',params)

    elif extraspaceremover == "on":
        analyzed = ""
        for i in range (1,len(djtext)):
            if djtext[i] == ' ' and djtext[i-1] == ' ':
                analyzed += djtext[i]
                i+=1
            else:
                analyzed += djtext[i]
        params = {'purpose': 'Extra Spaces Removed','analyzed_text':analyzed}

        return render(request,'analyze.html',params)

    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalizefirst")

# def newlineremove(request):
#     return HttpResponse("newlineremove")

# def spaceremove(request):
#     return HttpResponse("spaceremove <a href ='/'> back <a> ")
