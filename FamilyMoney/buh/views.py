from django.shortcuts import render
from django.http import HttpResponse
from .models import OverFunds, TransType, Trans, SourceMoney, Users
from django.db.models import F, Sum


def HomePageView(request):
    sources = SourceMoney.objects.all()
    total = SourceMoney.objects.aggregate(Sum('sum'))

    return render(request, 'buh/index.html', {
        'sources': sources,
        'total': total.get('sum__sum')
    })

def AddTransaction(request):
    sources = Trans.objects.all()

    return render(request, 'buh/add_trans.html', {
        'sources': sources

    })



