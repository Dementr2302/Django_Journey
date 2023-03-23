from django.shortcuts import render


def voucher(request):
    return render(request, 'voucher/voucher.html')

def infor(request):
    return render(request, 'voucher/infor.html')

