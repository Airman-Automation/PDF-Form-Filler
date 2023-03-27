
import email
import json
import re
from typing import Dict, List

from django.shortcuts import render, redirect
from django.http import HttpResponse
from arc_utils.pdf import Pdf
from arc_utils.mappings import mapping
from arc_utils.group_send_gmail import sendGmail
from arc_utils.group_send_outlook import sendOutlook


from .models import User, Form

# Create your views here.


def main(request):
    # return HttpResponse("hello world")
    context = {"pdf": Pdf("pdfs/FMAG_Form_Fillable.pdf").to_list()}
    return render(request, "test.html", context)


def got_form(request):
    print("Got form!")

    req = json.loads(request.body.decode("utf-8"))
    print(req)
    filename = req["filename"]
    filename = filename[filename.rfind("/") + 1:]
    del req["filename"]

    pdf = Pdf(f"pdfs/{filename}")

    for key, val in req.items():
        try:
            pdf.key_fill(key, val)
        except:
            print(f"{key} could not be filled")

    pdf.save("pdfs/response.pdf")

    return HttpResponse()

    # req = json.loads(request.body.decode("utf-8"))
    # print(req)

    # req = json.loads(request.body.decode("utf-8"))
    # pdf = Pdf("pdfs/FMAG_Form_Fillable.pdf")
    # pdf.bulk_fill(req.values())
    # pdf.save("pdfs/fmag_response.pdf")
    # return HttpResponse("hello world")


def list_users(request):
    context = {"users": [user.name for user in User.objects.only("name")]}
    return render(request, "user_list.html", context)


def list_forms(request):
    context = {
        "user": request.GET.get("user"),
        "forms": [form.name for form in Form.objects.only("name")]
    }
    return render(request, "form_select.html", context)


def upload_form(request):
    filename = str(request.FILES["new_file"])
    with open(f"pdfs/{filename}", "wb") as f:
        f.write(request.FILES["new_file"].file.read())
    Form(name=filename).save()
    # Form.objects.all().delete()
    return HttpResponse()


def autofill(user: User, filename: str) -> str:
    pdf = Pdf(f"pdfs/{filename}")
    for annot in pdf.annots:
        fillable_field = annot["/T"][1:-1]
        if fillable_field in mapping:
            attr = mapping[fillable_field]
            value = getattr(user, attr)
            if value is True:
                value = "On"
            elif value is False:
                value = "Off"
            pdf.key_fill(fillable_field, value)

    output_filepath = f"pdfs/{user}_template_{filename}"
    pdf.save(output_filepath)
    return output_filepath



def single_autofill(request):
    print("Got user!")

    req = json.loads(request.body.decode("utf-8"))
    print(req)
    user = User.objects.filter(name=req["user"]).first()
    filename = req["filename"]
    autofill(user, filename)

    return HttpResponse()


def group_autofill(request):
    print("Got group autofill request!")

    req = json.loads(request.body.decode("utf-8"))
    print(req)

    # filename = req["filename"]
    # filename = filename[filename.rfind("/") + 1:]
    filename = "response.pdf"

    for email in req["Gmail"]:
        user = User.objects.filter(email=email).first()
        output_filepath = autofill(user, filename)
        sendOutlook(email, output_filepath)
    
    for email in req["Outlook"]:
        user = User.objects.filter(email=email).first()
        output_filepath = autofill(user, filename)
        sendOutlook(email, output_filepath)
    
    return HttpResponse()


def group_send(request):
    req: Dict = json.loads(request.body.decode("utf-8"))
    print(req)
    if req["Gmail"]:
        sendGmail(req["Gmail"])
    if req["Outlook"]:
        sendOutlook(req["Outlook"])

    return HttpResponse()


def new_user_registration(request):
    return render(request, "register.html")


def save_new_user(request):
    # unpacks the json and save a new user to the sqlite database
    # User(...).save()
    req: Dict = json.loads(request.body.decode("utf-8"))
    print(req)

    # if req.get('us'):
    #     req['us'] == "On"
    # else:
    #     req['us'] == "Off"

    # if req.get('fn'):
    #     req['fn'] == "On"
    # else:
    #     req['fn'] == "Off"

    # if req.get('other'):
    #     req['other'] == "On"
    # else:
    #     req['other'] == "Off"

    # if req.get('military'):
    #     req['military'] == "On"
    # else:
    #     req['military'] == "Off"

    # if req.get('civilian'):
    #     req['civilian'] == "On"
    # else:
    #     req['civilian'] == "Off"

    # if req.get('contractor'):
    #     req['contractor'] == "On"
    # else:
    #     req['contractor'] == "Off"

    # if req.get('iatraining'):
    #     req['iatraining'] == "On"
    # else:
    #     req['iatraining'] == "Off"

    User(name=req["name"], rank=req["rank"],
         email=req["email"], dsn_phone=req["phonedsn"], organization=req["organization"], unit_mailing_address=req["mailingaddress"], citizenship_us=req["us"], citizenship_fn=req["fn"], citizenship_other=req["other"], designation_of_person_military=req["military"], designation_of_person_civilian=req["civilian"], designation_of_person_contractor=req["contractor"], ia_training_complete=req["iatraining"], ia_training_date=req["iadate"],).save()

    return HttpResponse()
