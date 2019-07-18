from rest_framework import serializers

from .models import PassportInfo


class PassPortSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = PassportInfo

        extra_kwargs = {
            'create_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        fields = ('id', 'owner', 'using_country', 'country_of_citizenship',
                  'passport_number', 'issue_date', 'expiration_date',
                  'passport_photo', 'created_at', 'updated_at',)
