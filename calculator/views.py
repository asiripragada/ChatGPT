from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
#from rest_framework.response import Response
import json


## Load the required libraries
import numpy as np
import pandas as pd

import os
import openai
# Create your views here.
import os
OPENAI_API_KEY= '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'

def Merge(dict1, dict2):
    return(dict2.update(dict1))

def index(request):
    return render(request, "input.html")


def addition(request):
    method = request.GET['method']
    text = request.GET['text']


    if not text.isdigit():
    
        text='food is good'
        openai.api_key = OPENAI_API_KEY
        
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt="Decide whether a Tweet's sentiment is positive, neutral, or negative.\n\nTweet:"+"'"+text+"'"+"\nSentiment:",
          temperature=0,
          max_tokens=60,
          top_p=1.0,
          frequency_penalty=0.5,
          presence_penalty=0.0,
        )
        
        sent={'method':'Sentiment'}

        Merge(sent,response)
        return JsonResponse(response, safe = False)

        #return render(request, "result.html", {"result": predictions1})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result": res})
