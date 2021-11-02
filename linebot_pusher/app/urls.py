from django.urls import path, re_path
from .views import Home, Test, Webhook_Line, Webhook_Pusher, History_Message

urlpatterns = [
    path('', Home),
    path('test', Test),
    path('webhook_line', Webhook_Line),
    path('webhook_pusher',Webhook_Pusher),
    path('history_message',History_Message),

    
]

