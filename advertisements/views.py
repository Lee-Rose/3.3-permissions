from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsAdOrReadOnly

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    default_permissions_class = ['IsAdminUser']
    authentication_classes = ['TokenAuthentication']
    # permission_classes = [IsAuthenticatedOrReadOnly, IsAdOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['created_at', 'status']

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdOrReadOnly]
        return [IsAuthenticatedOrReadOnly()]
