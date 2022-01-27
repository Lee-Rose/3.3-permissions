from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    default_permissions_class = [IsAdminUser]
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return [IsAuthenticatedOrReadOnly()]

    @api_view(['CREATE'])
    @permission_classes([IsAuthenticated])
    def create_new_ad(self,request, format=None):
        """создавать новое объявление могут только авторизированные пользователи """
