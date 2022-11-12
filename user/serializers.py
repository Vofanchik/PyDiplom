from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'patronymic', 'company', 'position']


class UserRegistrSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()


    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'patronymic', 'company', 'position', 'password', 'password2']


    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            patronymic=self.validated_data['patronymic'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            company=self.validated_data['company'],
            position=self.validated_data['position'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})

        user.set_password(password)
        user.save()

        return user