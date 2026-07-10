from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#simplejwt(for test popose)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #simplejwt(for test porpose)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    #product and category
    path('', include('productsApp.urls')),
    path('', include('categoriesApp.urls')),
    #cart and cartitem
    path('', include('cartApp.urls')),
    #orders
    path('', include('ordersApp.urls')),
    #account (auth)
    path('api/user/', include('accountApp.urls')),
    #payment
    path('',include('paymentsApp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, documents_roots=settings.MEDIA_ROOT)
