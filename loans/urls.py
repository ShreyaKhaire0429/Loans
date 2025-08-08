# from django.urls import path
# from . import views

# urlpatterns = [
#     path('register', views.RegisterCustomer.as_view()),
#     path('check-eligibility', views.CheckEligibility.as_view()),
#     path('create-loan', views.CreateLoan.as_view()),
#     path('view-loan/<int:loan_id>', views.ViewLoan.as_view()),
#     path('view-loans/<int:customer_id>', views.ViewCustomerLoans.as_view()),
# ]

# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# urlpatterns += [
#     # API schema
#     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
#     # Swagger UI
#     path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
#     # Redoc UI (optional)
#     path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
# ]

# from django.contrib import admin
# from django.urls import path, include
# from drf_spectacular.views import (
#     SpectacularAPIView,
#     SpectacularSwaggerView,
#     SpectacularRedocView,
# )

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("api/", include("loans.urls")),

#     # path("api/", include("your_app.urls")),   # your APIs
#     path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
#     path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
#     path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterCustomerView.as_view(), name='register'),
    path('check-eligibility/', views.CheckEligibility.as_view(), name='check-eligibility'),
    path('create-loan/', views.CreateLoan.as_view(), name='create-loan'),
    path('view-loan/<int:loan_id>/', views.ViewLoan.as_view(), name='view-loan'),
    path('view-loans/<int:customer_id>/', views.ViewCustomerLoans.as_view(), name='view-loans'),
]
