from django.urls import path, include
from reviews_app.api.views import ReviewListView, ReviewCreateView, ReviewDetailView

urlpatterns = [
    path('game/<int:pk>/reviews', ReviewListView.as_view(), name='review-list'),
    path('game/<int:pk>/reviews/create', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
    
]
