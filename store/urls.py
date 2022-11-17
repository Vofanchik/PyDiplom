from django.urls import path

from store.views import PartnerUpdate, ShopView, ProductInfoView, BasketView, ContactView, OrderView

urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('shops', ShopView.as_view(), name='shops'),
    path('products', ProductInfoView.as_view(), name='shops'),
    path('basket', BasketView.as_view(), name='basket'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('order', OrderView.as_view(), name='order'),
]