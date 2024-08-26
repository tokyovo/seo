from django.urls import path
from .views import HomePageView, UserMessageView, BotMessageView, HistoryMessageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('api/users/message', UserMessageView.as_view(), name='user-message'),
    path('api/bot/message', BotMessageView.as_view(), name='bot-message'),
    path('api/history/message', HistoryMessageView.as_view(), name='history-message'),
]
