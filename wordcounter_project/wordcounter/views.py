from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')


def count(request):
    fulltext=request.GET['fulltext'] #this will fetch the input from the textbox and store in fulltext
    # print(fulltext) #to print in the terminal
    wordlist=fulltext.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word]+=1
        else:
            #AddtoDictionary
            worddictionary[word]=1

    sortedcount=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'wordcount':len(wordlist),'sortedcount':sortedcount})


def about(request):
    return render(request,'about.html')




