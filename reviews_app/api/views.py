from django.forms import ValidationError
from rest_framework import generics
from reviews_app.api.serializers import ReviewSerializer
from reviews_app.models import Review
from games_app.models import Game
from games_app.api import permissions

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(game=pk)
class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        game = Game.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(game=game)
        if review_queryset.exists():
            raise ValidationError('You have already reviewd this movie')
        serializer.save(game=game, user=review_user)
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.ReviewUserOrReadOnly]