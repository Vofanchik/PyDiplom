from django.urls import path

from store.views import PartnerUpdate, ShopView, ProductInfoView

urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('shops', ShopView.as_view(), name='shops'),
    path('products', ProductInfoView.as_view(), name='shops'),
]