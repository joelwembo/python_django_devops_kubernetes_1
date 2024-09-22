# from django.contrib.auth.password_validation import validate_password
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from .models import MyUser
# from django.core.validators import FileExtensionValidator


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         token['email'] = user.email
#         token['bio'] = user.bio
#         # ...

#         return token


# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=MyUser.objects.all())]
#     )
#     cover_photo = serializers.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),], required=False)

#     class Meta:
#         model = MyUser
#         fields = ('username', 'email', 'password', 'password2', 'bio', 'cover_photo')

#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError(
#                 {"password": "Password fields didn't match."})
#         if 'cover_photo' in attrs and attrs['cover_photo'] is not None and attrs['cover_photo'].size > 1024 * 1024:
#             raise serializers.ValidationError(
#                 {"cover_photo": "The file size must be less than 1 MB."})

#         return attrs

#     def create(self, validated_data):
#         cover_photo = validated_data.get('cover_photo')
#         user = MyUser.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             bio=validated_data['bio'],
#             cover_photo=cover_photo
#     )
#         user.set_password(validated_data['password'])
#         user.save()
        
#         return user

