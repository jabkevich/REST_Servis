from rest_framework import viewsets, permissions, status
from .serializers import *


class WalletViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Wallet.objects.all()
        owner = self.request.query_params.get('owner', None)
        if owner is not None:
            queryset = queryset.filter(owner=owner)
        return queryset

    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = WalletSerializer


class ViewGet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = History.objects.all()
        wallet = self.request.query_params.get('wallet', None)
        if wallet is not None:
            print(wallet)
            queryset = queryset.filter(wallet=wallet)
        return queryset

    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = HistorySerializer


# class TransactionViewSet(viewsets.ModelViewSet):
#     def get_queryset(self):
#         queryset = Transaction.objects.all()
#         owner = self.request.user
#         queryset = queryset.filter(owner=owner)
#         return queryset
#
#     permissions_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = TransactionSerializer
