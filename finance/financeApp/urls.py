from rest_framework import routers

from .api import *

router = routers.DefaultRouter()
router.register('api/wallet', WalletViewSet, 'wallet')
router.register('api/history', ViewGet, 'history')
# router.register('api/transaction', TransactionViewSet, 'transaction')


urlpatterns = router.urls
