# # from rest_framework import serializers
# # from .models import Customer, Loan

# # class CustomerRegisterSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Customer
# #         fields = ['first_name', 'last_name', 'age', 'phone_number', 'monthly_salary', 'email']

# # class CustomerSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Customer
# #         fields = '__all__'

# # class CheckEligibilitySerializer(serializers.Serializer):
# #     customer_id = serializers.IntegerField()
# #     loan_amount = serializers.FloatField()
# #     interest_rate = serializers.FloatField()
# #     tenure = serializers.IntegerField()

# # class EligibilityResultSerializer(serializers.Serializer):
# #     credit_score = serializers.IntegerField()
# #     is_eligible = serializers.BooleanField()
# #     approved_limit = serializers.FloatField()
# #     message = serializers.CharField()

# # class CreateLoanSerializer(serializers.Serializer):
# #     customer_id = serializers.IntegerField()
# #     loan_amount = serializers.FloatField()
# #     interest_rate = serializers.FloatField()
# #     tenure = serializers.IntegerField()

# # class LoanSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Loan
# #         fields = '__all__'

# from rest_framework import serializers
# from .models import Customer, Loan

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = '__all__'

# class LoanSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Loan
#         fields = '__all__'

# # For /register
# class RegisterSerializer(serializers.Serializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     phone_number = serializers.CharField()
#     age = serializers.IntegerField()
#     monthly_income = serializers.FloatField()

# # For /check-eligibility and /create-loan
# class LoanCheckSerializer(serializers.Serializer):
#     customer_id = serializers.IntegerField()
#     loan_amount = serializers.FloatField()
#     interest_rate = serializers.FloatField()
#     tenure = serializers.IntegerField()

from rest_framework import serializers
from .models import Customer, Loan

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField()
    monthly_income = serializers.DecimalField(max_digits=12, decimal_places=2)
    phone_number = serializers.CharField()

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"

class CheckEligibilitySerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    loan_amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = serializers.DecimalField(max_digits=5, decimal_places=2)
    tenure = serializers.IntegerField()
