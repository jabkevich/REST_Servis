

# Wallet
## ViewSet
```
class WalletViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Wallet.objects.all()
        owner = self.request.user
        if self.request.successful_authenticator:
            queryset = queryset.filter(owner=owner)
            return queryset
    
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = WalletSerializer
```
## serializer
```
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

    def update(self, instance, validated_data):
        addTransactionHistory(instance, validated_data)
        instance.updateName(validated_data.get('name', instance.name))
        return instance
```




# History
## ViewGet
```
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

    def update(self, instance, validated_data):
        addTransactionHistory(instance, validated_data)
        instance.updateName(validated_data.get('name', instance.name))
        return instance
```


##serializer

```
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('data', 'sum', 'wallet', "typeOfTransaction", "description", "id")
        read_only_fields = ('data', 'sum', 'wallet', "typeOfTransaction", "description")

```
