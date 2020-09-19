# I have created this file - Alfaiz
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# def index(request):
#     return HttpResponse('<h1>This is Index Page</h1> <a href="https://www.google.co.in" target="_blank">Google</a> <a href="https://www.facebook.com/" target="_blank">Facebook</a> <a href="https://www.youtube.com/" target="_blank">Youtube</a> <a href="https://www.instagram.com/?hl=en" target="_blank">Instagram</a> <a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/" target="_blank">Python Packages For Windows</a>')

# def about(request):
#     return HttpResponse('<h1>This is About Page</h1>')


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text.
    az_textarea = request.GET.get('index_textarea', 'default')

    # Check Checkbox Values
    rp_check = request.GET.get('rp_checkbox', 'off')
    cf_check = request.GET.get('cf_checkbox', 'off')
    nlr_check = request.GET.get('nlr_checkbox', 'off')
    sr_check = request.GET.get('sr_checkbox', 'off')

    # Check Which Checkbox is on:

    # Remove Punctuation Code:
    if rp_check == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in az_textarea:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        az_textarea = analyzed

    # Capitalized First/Uppercase Code:
    if(cf_check == "on"):
        analyzed = ""

        for char in az_textarea:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        az_textarea = analyzed

    # New Line Remover Code:
    if(nlr_check == "on"):
        analyzed = ""

        for char in az_textarea:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        az_textarea = analyzed

    # Space Remover Code:
    if(sr_check == "on"):
        analyzed = ""

        for index, char in enumerate(az_textarea):
            if not(az_textarea[index] == " " and az_textarea[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}

    # Error Page
    if(rp_check != "on" and cf_check != "on" and nlr_check != "on" and sr_check != "on"):
        return HttpResponse('<h1>ERROR!!!</h1><br><h1>Please Select Atleast Any Operation With Some Text...</h1>')

    return render(request, 'analyze.html', params)
