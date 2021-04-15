from decimal import Decimal

from django.db import transaction
from rest_framework import serializers
from .models import *


def addTransactionHistory(instance, validated_data):
    with transaction.atomic():
        plus_amount = validated_data.get('amount', instance.amount)
        id = validated_data.get('id', instance.id)
        if Wallet.objects.filter(id=id).first().amount + plus_amount < 0:
            raise serializers.ValidationError('negative amount')
        else:
            instance.updateAmount(plus_amount)
            if plus_amount < 0:
                typeOfTransaction = "debiting"
            else:
                typeOfTransaction = "replenishment"
            History.objects.create(description='', sum=plus_amount, wallet=instance,
                                   typeOfTransaction=typeOfTransaction)


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

    def update(self, instance, validated_data):
        addTransactionHistory(instance, validated_data)
        instance.updateName(validated_data.get('name', instance.name))
        return instance


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('data', 'sum', 'wallet', "typeOfTransaction", "description", "id")
        read_only_fields = ('data', 'sum', 'wallet', "typeOfTransaction", "description")

# class TransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = '__all__'
#
#     def create(self, validated_data):
#         print(validated_data)
#         print(validated_data.get('walletFrom').id)
#         print(validated_data.get('walletTo').id)
#         name = validated_data.get('walletFrom').name
#         amount = validated_data.get('walletFrom').amount
#         owner = validated_data.get('walletFrom').owner
#         Wallet.objects.get(id=validated_data.get('walletFrom').id).update(field={'name':name, 'amount': -amount, 'owner': owner})
#         name = validated_data.get('walletTo').name
#         amount = validated_data.get('walletTo').amount
#         owner = validated_data.get('walletTo').owner
#         Wallet.objects.get(id=validated_data.get('walletTo').id).update(field={'name':name, 'amount': amount, 'owner': owner})
#
#         return validated_data
