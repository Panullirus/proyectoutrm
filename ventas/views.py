from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import pymongo
from bs4 import BeautifulSoup
import requests

client = pymongo.MongoClient("mongodb+srv://m001-student:Pakito24@sandbox.cbqx4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['test']
col = db['test1']

def home(request):
    return render(request,'ejercicio/home.html',{"database":col.find({})})