from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    analyzed = ""

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'removed puctuations','analyzed_text':analyzed }
        djtext = analyzed
    if newlineremover == "on":
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'newlineremover', 'analyzed_text': analyzed}
        djtext = analyzed
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
             if djtext[index] == " " and djtext[index + 1] == " ":
                pass
             else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        djtext = analyzed
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        # djtext = analyzed
    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("Please select any operation")

    return render(request,'analyze.html', params)

