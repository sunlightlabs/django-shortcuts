from shortcuts.models import Shortcut
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, render_to_response

def redirect(request, alias):
    
    sc = get_object_or_404(Shortcut, alias=alias)
    
    if sc.method == 'http301':
        return HttpResponsePermanentRedirect(sc.redirect_to)
    elif sc.method == 'http302':
        return HttpResponseRedirect(sc.redirect_to)
    elif sc.method == 'meta':    
        return render_to_response('shortcuts/redirect.html', {'shortcut': sc})

    return HttpResponse('')
    