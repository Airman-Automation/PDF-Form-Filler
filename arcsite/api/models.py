from django.db import models

# Create your models here.


class User(models.Model):
    # name = models.TextField() # Last, First, Middle Initial
    # job_title = models.TextField()
    # office_symbol = models.TextField()
    name = models.TextField()  # Last, First, Middle Initial
    rank = models.TextField()
    dodin = models.TextField()  # What is DODIN?
    social_security_number = models.TextField()
    dafsc = models.TextField()  # What is DAFSC?
    email = models.TextField()
    dsn_phone = models.TextField()
    commercial_phone = models.TextField()
    organization = models.TextField()
    unit_mailing_address = models.TextField()
    # What is Duty Title? postion you fill within the unit, ie commander director, cheif of commander of inovations
    duty_title = models.TextField()
    designation_of_person_military = models.BooleanField()
    designation_of_person_civilian = models.BooleanField()
    designation_of_person_contractor = models.BooleanField()
    citizenship_us = models.BooleanField()
    citizenship_fn = models.BooleanField()
    citizenship_other = models.BooleanField()
    ia_training_complete = models.BooleanField()
    ia_training_date = models.TextField()

    # Example:
    # name = Doe, John I.
    # office_symbol = ADO
    # job_title = CHIEF, COMMANDER'S INNOVATION

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.TextField()


"""
(Initial Check Box)
(Modification Check Box)
(Deactivate Check Box)
(User ID Check Box)
(User ID Field)
(Date Requested Field)
(System Name Field)
(System Location Field)
(1 Members Name Field)
(2 Members Organization Field)
(3 Members Office Symbol Field)
(4 Members Phone Number Field)
(5 Members Email Field)
(6 Members Duty Title & Grade Field)
(7 Members Official Address Field)
(1 US Check Box)
(2 FN Check Box)
(3 Other Check Box)
(1 Military Check Box)
(2 Civilian Check Box)
(3 Contractor Check Box)
(10 IA Training Requirements Check Box)
( IA Training Completion Date Field)
(11 Members Signature)
(12 Date Member Signed)
(13 Justification for Access Field)
(14a Authorized)
(14b Privileged)
(15 REQUIRED ACCESS - UNCLASSIFIED)
(15 REQUIRED ACCESS - CLASSIFIED)
(15 REQUIRED ACCESS - OTHER)
(15 REQUIRED ACCESS - OTHER DESCRIPTION)
(16 NTK VERIFICATION)
(16a ACCESS EXPIRATION DATE)
(17 Supervisors Name Field)
(18 SUPERVISORS SIGNATURE)
(19 DATE SUPERVISOR SIGNED)
(20 Supervisors Organization field)
(20a Supervisors Email Field)
(20b Supervisors Phone Field)
( SIGNATURE OF INFORMATION OWNER)
( IO PHONE NUMBER)
( IO DATE)
( SIGNATURE OF IAO)
( IAO ORGANIZATION/DEPARTMENT)
( IAO PHONE NUMBER)
( DATE IAO SIGNED)
( MEMBERS NAME)
( OPTIONAL INFORMATION)
( TYPE OF INVESTIGATION)
( DATE OF INVESTIGATION)
( CLEARANCE LEVEL)
( IT LEVEL DESGINATION - I)
( IT LEVEL DESGINATION - II)
( IT LEVEL DESGINATION - III)
( SECURITY MANAGERS NAME)
( SECURITY MANAGERS NUMBER)
( SECURITY MANAGER SIGNATURE)
( DATE SECURITY MANAGER SIGNED)
(TITLE 1)
(SYSTEM)
(SYSTEM ACCOUNT CODE)
(TITLE 2)
(DOMAIN)
(DOMAIN ACCOUNT CODE)
(TITLE 3)
(SERVER)
(SERVER ACCOUNT CODE)
(TITLE 4)
(APPLICATION)
(APPLICATION ACCOUNT CODE)
(TITLE 5)
(DIRECTORIES)
(DIRECTORIES ACCOUNT CODE)
(TITLE 6)
(FILES)
(FILES ACCOUNT CODE)
(TITLE 7)
(DATASETS)
(DATASETS ACCOUNT CODE)
(PROCESSED BY)
(DATE REVALIDATED)
(REVALIDATED BY)
(DATE SIGNED)
(RESET)
"""
