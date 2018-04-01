from datetime import datetime
from django.db.models.functions import TruncMonth
from django.db.models import Sum

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView

from .serializers import ExpenseSerializer, CategorySerializer
from .models import Expense, Category


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.order_by('created_date').all()
    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.order_by('created_date').all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class CollectSubmissionsView(APIView):
    def get(self, ):
        today = datetime.now()
        queryset = Expense.objects.filter(
            created_date__year=today.year,
            created_date__month=today.month
        ).aggregate(Sum('amount'))
