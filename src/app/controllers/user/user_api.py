from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        access = refresh.access_token
        
        
        response_data = {
            'success': True,
            'message': "",
            'status_code': status.HTTP_201_CREATED,
            'message_code': "",
            'dev_message': "",
            'data': {
                'access': str(access),
                'expires': access['exp'],
                'expires_refresh_token': refresh['exp'],
                'refresh': str(refresh),
                'profile': {
                    'user_id': self.user.id,
                    'user_name': self.user.user_name,
                    'email': self.user.email,
                    'Company_id': self.user.company_id
                }
            }
        }

        return response_data

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        access = data['access']
        response_data = {
            'success': True,
            'message': "",
            'status_code': status.HTTP_201_CREATED,
            'message_code': "",
            'dev_message': "",
            'data': {
                'access': str(access)
            }
        }

        return response_data
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer

