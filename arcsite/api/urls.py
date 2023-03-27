from django.urls import path
from .views import (
    main,
    got_form,
    list_users,
    single_autofill,
    group_autofill,
    group_send,
    new_user_registration,
    save_new_user,
    list_forms,
    upload_form,
)

app_name = "api"

urlpatterns = [
    path('', main),
    path('resp', got_form),
    path('users', list_users, name="list_users"),
    path('fill', single_autofill),
    path('group_fill', group_autofill),
    path('email', group_send),
    path('register', new_user_registration, name="new_user_registration"),
    path('savenewuser', save_new_user),
    path('forms', list_forms, name="list_forms"),
    path('upload', upload_form),
]
