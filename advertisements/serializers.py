from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )
        read_only_fields = ['creator']

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        get_status = data.get('status')
        if get_status in ['OPEN', 'Открыто'] \
        or self.context['request'].method == 'POST':
             advs_user = data.creator.all('status').filter('OPEN')
             if advs_user.count('OPEN') > 10:
                 return serializers.ValidationError('You can not have more than 10 open ads')
        return data






