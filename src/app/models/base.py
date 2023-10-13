from django.db import models


# Create your models here.

#BaseModel
#----------------------------------------------------------------
class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    company_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ActivityLog(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    company_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    action = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


#Terms Type
#----------------------------------------------------------------
class TERMTYPE:
    DAY = 'DAY'
    WEEK = 'WEEK'
    MONTH = 'MONTH'
    QUARTER = 'QUARTER'
    YEAR = 'YEAR'
    
    CHOICES = (
        ( DAY, 'Ngày' ),
        ( WEEK, 'Tuần' ),
        ( MONTH, 'Tháng' ),
        ( QUARTER, 'Quý' ),
        ( YEAR, 'Năm' )
    )

#Payment Method
#----------------------------------------------------------------
class PaymentMethod:
    CASH = 'CASH'
    CREDIT_CARD = 'CREDITCARD'

    CHOICES = (
        ( CASH, 'Tiền mặt' ),
        ( CREDIT_CARD, 'Thẻ tín dụng' ),
    )