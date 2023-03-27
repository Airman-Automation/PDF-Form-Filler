"""
Mapping of PDF annotation name (i.e. '/T' field) to a the User model's
attribute for corresponding data. Use these mappings to checking if and how
a field can be autofilled.
"""

mapping = {
    "1 Members Name Field": "name",
    "6 Members Duty Title & Grade Field": "rank",
    # "": "dodin", company id, user id
    # "": "social_security_number",
    # "": "dafsc", 11s
    "5 Members Email Field": "email",
    "4 Members Phone Number Field": "dsn_phone",
    # "4 Members Phone Number Field": "commercial_phone",
    "2 Members Organization Field": "organization",
    "7 Members Official Address Field": "unit_mailing_address",
    # "": "duty_title",
    "1 Military Check Box": "designation_of_person_military",
    "2 Civilian Check Box": "designation_of_person_civilian",
    "3 Contractor Check Box": "designation_of_person_contractor",
    "1 US Check Box": "citizenship_us",
    "2 FN Check Box": "citizenship_fn",
    "3 Other Check Box": "citizenship_other",
    "10 IA Training Requirements Check Box": "ia_training_complete",
    " IA Training Completion Date Field": "ia_training_date",
}

"""
For reference: all fields from envision.pdf

>>> for annot in p.annots:
...     print(annot["/T"])
... 
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
