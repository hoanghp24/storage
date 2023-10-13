#django restframework
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny

#helpers
from app.helpers.response import GetSuccess

#models
from app.models.base import TERMTYPE, PaymentMethod

#serializers
from app.serializers.enum import EnumChoiceSerializer



# Create your API here.

#Enum API
#----------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_enum_values(request):
    term_type_choices = TERMTYPE.CHOICES
    payment_method_choices = PaymentMethod.CHOICES

    term_type_serializer = EnumChoiceSerializer([
        {'value': choice[0], 'display_name': choice[1]} for choice in term_type_choices
    ], many=True)

    payment_method_serializer = EnumChoiceSerializer([
        {'value': choice[0], 'display_name': choice[1]} for choice in payment_method_choices
    ], many=True)

    return GetSuccess({
        'term_types': term_type_serializer.data,
        'payment_methods': payment_method_serializer.data,
    })
