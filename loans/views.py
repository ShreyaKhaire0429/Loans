# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Customer, Loan
# from .serializers import (
#     CustomerSerializer,
#     LoanSerializer,
#     RegisterSerializer,
#     LoanCheckSerializer
# )
# from datetime import date

# class RegisterCustomer(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             data = serializer.validated_data
#             approved_limit = round((data['monthly_income'] * 36) / 100000) * 100000
#             customer = Customer.objects.create(
#                 first_name=data['first_name'],
#                 last_name=data['last_name'],
#                 phone_number=data['phone_number'],
#                 age=data['age'],
#                 monthly_income=data['monthly_income'],
#                 approved_limit=approved_limit
#             )
#             return Response(CustomerSerializer(customer).data)
#         return Response(serializer.errors, status=400)

# class CheckEligibility(APIView):
#     def post(self, request):
#         serializer = LoanCheckSerializer(data=request.data)
#         if serializer.is_valid():
#             data = serializer.validated_data
#             customer = Customer.objects.get(id=data['customer_id'])
#             loans = Loan.objects.filter(customer=customer)

#             credit_score = 100
#             total_loan_amount = sum(l.loan_amount for l in loans)
#             if customer.current_debt > customer.approved_limit:
#                 credit_score = 0

#             approval = False
#             corrected_interest_rate = data['interest_rate']

#             if credit_score > 50:
#                 approval = True
#             elif 30 < credit_score <= 50 and data['interest_rate'] >= 12:
#                 approval = True
#             elif 10 < credit_score <= 30 and data['interest_rate'] >= 16:
#                 approval = True
#             else:
#                 approval = False

#             if credit_score <= 30 and data['interest_rate'] < 16:
#                 corrected_interest_rate = 16
#             elif credit_score <= 50 and data['interest_rate'] < 12:
#                 corrected_interest_rate = 12

#             emi = (data['loan_amount'] * (1 + corrected_interest_rate / 100) ** data['tenure']) / data['tenure']

#             return Response({
#                 "customer_id": customer.id,
#                 "approval": approval,
#                 "interest_rate": data['interest_rate'],
#                 "corrected_interest_rate": corrected_interest_rate,
#                 "tenure": data['tenure'],
#                 "monthly_installment": round(emi, 2)
#             })
#         return Response(serializer.errors, status=400)

# class CreateLoan(APIView):
#     def post(self, request):
#         serializer = LoanCheckSerializer(data=request.data)
#         if serializer.is_valid():
#             data = serializer.validated_data
#             customer = Customer.objects.get(id=data['customer_id'])
#             emi = (data['loan_amount'] * (1 + data['interest_rate'] / 100) ** data['tenure']) / data['tenure']
#             loan = Loan.objects.create(
#                 customer=customer,
#                 loan_amount=data['loan_amount'],
#                 tenure=data['tenure'],
#                 interest_rate=data['interest_rate'],
#                 monthly_installment=emi,
#                 emis_paid_on_time=0,
#                 end_date=date.today().replace(year=date.today().year + data['tenure'])
#             )
#             return Response({
#                 "loan_id": loan.id,
#                 "customer_id": customer.id,
#                 "loan_approved": True,
#                 "message": "Loan approved and created",
#                 "monthly_installment": round(emi, 2)
#             })
#         return Response(serializer.errors, status=400)

# class ViewLoan(APIView):
#     def get(self, request, loan_id):
#         loan = Loan.objects.get(id=loan_id)
#         return Response({
#             "loan_id": loan.id,
#             "customer": {
#                 "id": loan.customer.id,
#                 "first_name": loan.customer.first_name,
#                 "last_name": loan.customer.last_name,
#                 "phone_number": loan.customer.phone_number,
#                 "age": loan.customer.age,
#             },
#             "loan_amount": loan.loan_amount,
#             "interest_rate": loan.interest_rate,
#             "monthly_installment": loan.monthly_installment,
#             "tenure": loan.tenure,
#         })

# class ViewCustomerLoans(APIView):
#     def get(self, request, customer_id):
#         loans = Loan.objects.filter(customer_id=customer_id)
#         data = []
#         for loan in loans:
#             data.append({
#                 "loan_id": loan.id,
#                 "loan_amount": loan.loan_amount,
#                 "interest_rate": loan.interest_rate,
#                 "monthly_installment": loan.monthly_installment,
#                 "repayments_left": loan.tenure - loan.emis_paid_on_time
#             })
#         return Response(data)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, CustomerSerializer, LoanSerializer, CheckEligibilitySerializer
from .models import Customer, Loan

# -----------------------------
# Register Customer API
# -----------------------------
class RegisterCustomerView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            # Save customer
            customer = Customer.objects.create(
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                age=serializer.validated_data['age'],
                monthly_income=serializer.validated_data['monthly_income'],
                phone_number=serializer.validated_data['phone_number']
            )

            return Response(
                {
                    "customer_id": customer.id,
                    "message": "Customer registered successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# Check Eligibility API
# -----------------------------
class CheckEligibility(APIView):
    def post(self, request):
        serializer = CheckEligibilitySerializer(data=request.data)

        if serializer.is_valid():
            customer_id = serializer.validated_data['customer_id']
            loan_amount = serializer.validated_data['loan_amount']
            interest_rate = serializer.validated_data['interest_rate']
            tenure = serializer.validated_data['tenure']

            # Example eligibility check (customize this logic)
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

            if customer.monthly_income >= 20000:
                return Response({"eligible": True, "message": "Customer is eligible for loan"})
            else:
                return Response({"eligible": False, "message": "Monthly income too low"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# Create Loan API
# -----------------------------
class CreateLoan(APIView):
    def post(self, request):
        serializer = LoanSerializer(data=request.data)

        if serializer.is_valid():
            loan = serializer.save()
            return Response(
                {"loan_id": loan.id, "message": "Loan created successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# View Loan by loan_id
# -----------------------------
class ViewLoan(APIView):
    def get(self, request, loan_id):
        try:
            loan = Loan.objects.get(id=loan_id)
        except Loan.DoesNotExist:
            return Response({"error": "Loan not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LoanSerializer(loan)
        return Response(serializer.data)


# -----------------------------
# View All Loans for a Customer
# -----------------------------
class ViewCustomerLoans(APIView):
    def get(self, request, customer_id):
        loans = Loan.objects.filter(customer_id=customer_id)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)
