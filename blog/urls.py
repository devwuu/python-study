from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view())
    # path variable 이름을 pk로 정해줘야 CBV를 사용할 수 있다
]