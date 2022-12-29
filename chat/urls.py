from rest_framework.routers import DefaultRouter
from chat.views import HTMXMessage

router = DefaultRouter()
router.register('hx', HTMXMessage)
