from django.shortcuts import render, HttpResponseRedirect

# Create your views here.


def started_redirect(request):
    # todo: redirect to name url
    return HttpResponseRedirect(request, name="")
