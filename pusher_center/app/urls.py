from django.urls import path, re_path
from .views import Home, Webhook_Pusher, Pusher_Authentication, History_Message, AllMember

urlpatterns = [
    path('', Home),
    path('webhook_pusher',Webhook_Pusher),
    path('pusher/auth',Pusher_Authentication),
    path('history_message',History_Message),
    path('allmember',AllMember),
]

