from django.http import HttpResponse
#to use templates
from django.shortcuts import render

def index(req):
    return render(req,'index.html')

def check1(text):
    analyzed=""
    punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    for char in text:
        if char not in punctuations:
            analyzed = analyzed+char
    return analyzed

def check2(text):
    analyzed=""
    for char in text:
        analyzed = analyzed + char.upper()
    return analyzed

def check3(text):
    analyzed = ""
    for char in text:
        if char != "\n" and char !="\r":
            analyzed += char
    return analyzed


def check4(text):
    analyzed=""
    for index,char in enumerate(text):
        if not(text[index] == ' ' and text[index+1]==' '):
            analyzed = analyzed + char
    return analyzed

def charCounter(text):
    count = 0
    for char in text:
        count = count + 1
    return count

def analyze(req):
    #getting the text
    djtext = req.POST.get('text','deafult')
    checkValue1 = req.POST.get('removepunc','off')
    checkValue2 = req.POST.get('fullcapital','off')
    checkValue3 = req.POST.get('newlinermv','off')
    checkValue4 = req.POST.get('spacermv','off')
    checkValue5 = req.POST.get('charcount','off')
    analyzed = djtext
    boolArray = [checkValue1,checkValue2,checkValue3,checkValue4]
    if checkValue5=="off":
        if checkValue1=="off" and checkValue1=="off" and checkValue2=="off" and checkValue3=="off" and checkValue4=="off":
            return HttpResponse("error")
        functions = {
            'off': lambda x: x,  # No operation function
            '1': check1,
            '2': check2,
            '3': check3,
            '4': check4
        }
        for i in range(len(boolArray)):
            if boolArray[i] == "on":
                analyzed = functions[str(i+1)](analyzed)
        params = {'purpose':'Count Number of Characters','analyzed_text':analyzed}
        return render(req,'analyze.html',params)
    else:
        count = charCounter(djtext)
        params = {'purpose':'Count Number of Characters','analyzed_text':count}
        return render(req,'analyze.html',params) 

def feedback(req):
    return render(req,'feedback.html')

def about(req):
    return render(req,'about.html')