from django.urls import path,include
from rest_framework import routers
from .views import NoteViewSet,RegisterViewSet
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'notes',NoteViewSet)
router.register(r'register',RegisterViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('token/',jwt_views.TokenObtainPairView.as_view()),
    path('token/refresh',jwt_views.TokenRefreshView.as_view()),
    path('token/verify',jwt_views.TokenVerifyView.as_view()),
]
