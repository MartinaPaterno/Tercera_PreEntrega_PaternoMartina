from django.urls import path
from .views import *

urlpatterns = [
    path('inbox/', ConversacionListView.as_view(), name='Inbox'),
    path('nuevoMsj/', ConversacionCreateView.as_view(), name='CrearConversacion'),
    path('<int:room_id>', ConversacionDetailView.as_view(), name='VerConversacion'),
    path('<int:pk>/agregar/', AgregarMensajeConversacionView.as_view(), name='AgregarMensaje'),
]