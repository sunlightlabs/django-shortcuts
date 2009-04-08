from shortcut.models import Shortcut
from django.shortcuts import render_to_response

def redirect(request, alias):
    try:
        sc = Shortcut.objects.get(alias=alias)
        sc.is_valid = True
    except Shortcut.DoesNotExist:
        sc = {
            "alias": alias,
            "redirect": request.path,
            "interval": 60,
            "title": "INVALID SHORTCUT ALIAS: %s" % alias,
            "analytics": None,
            "is_valid": False,
        }
    return render_to_response('shortcuts/redirect.html', {'shortcut': sc})