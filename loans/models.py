from django.db import models
from django.utils import timezone

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    age        = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, unique=True)
    monthly_salary = models.DecimalField(max_digits=12, decimal_places=2)
    approved_limit = models.BigIntegerField(default=0)
    current_debt = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    tenure = models.IntegerField(help_text='months')
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text='annual %')
    monthly_installment = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    emi_paid_on_time = models.IntegerField(default=0)  # number or percent; used in scoring
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def repayments_left(self):
        if not self.end_date or not self.start_date:
            return None
        today = timezone.now().date()
        if today > self.end_date:
            return 0
        total_months = (self.end_date.year - self.start_date.year) * 12 + (self.end_date.month - self.start_date.month)
        # Basic estimate:
        return max(total_months, 0)
