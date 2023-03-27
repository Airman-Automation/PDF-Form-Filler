from django.shortcuts import render

# Create your views here.
import json

from django.shortcuts import render
from django.http import HttpResponse
from arc_utils.pdf import Pdf
from api.models import User

# Create your views here.
def viewer(request):
    context = {
        "users": {
            user.email: user.name for user in User.objects.only("name", "email")
        },
        "filename": request.GET.get("file"),
    }

    response = render(request, "web/viewer.html", context)

    # Disable caching
    # https://stackoverflow.com/questions/728616/disable-cache-for-some-images
    response["Pragma-directive"] = "no-cache"
    response["Cache-directive"] = "no-cache"
    response["Cache-control"] = "no-cache"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"
    return response

    # return render(request, "web/viewer.html?file=%2Fassets%2Fenvision.pdf")
    # print(request.META["QUERY_STRING"])
    # return render(request, "pdf_viewer.html")

def got_form(request):
    # print(json.loads(request.body.decode("utf-8")))
    print("Got form!")
    req = json.loads(request.body.decode("utf-8"))
    pdf = Pdf("pdfs/FMAG_Form_Fillable.pdf")
    pdf.bulk_fill(req.values())
    pdf.save("pdfs/fmag_response.pdf")
    return HttpResponse("hello world")