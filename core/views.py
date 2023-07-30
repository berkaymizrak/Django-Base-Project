from django.shortcuts import render


# Create your views here.


def csrf_failure(request, reason=''):
    context = {
        'reason': reason,
    }
    return render(request, '403.html', context=context)
