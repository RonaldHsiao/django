from django.shortcuts import render
from django.http import HttpResponse

stocks=[
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
    ]


# Create your views here.
def index(request):
    str1 = "Hello django!"
    return HttpResponse(str1)


def get_stocks(request):
    for stock in stocks:
        print(f'{stock["分類"]}-{stock["指數"]}')
    return render(request,"stocks.html",{"stocks":stocks})