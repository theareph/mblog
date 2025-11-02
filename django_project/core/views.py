from django.conf import settings
from django.shortcuts import redirect, render

from . import models

# Create your views here.


def homepage(request):
    return render(
        request,
        "core/index.html",
        {
            "posts": models.Post.objects.order_by("-inserted_at")[:10],
        },
    )


def favicon(request):
    return redirect(
        request.build_absolute_uri(f"{settings.STATIC_URL}favicon.ico"),
    )
