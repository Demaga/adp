from rest_framework.serializers import ModelSerializer

from .models import Sub

class SubSerializer(ModelSerializer):
	
	class Meta:
		model = Sub
		fields = ['id', 'name', 'subscribed_date', 'days', 'is_staff', 'active'] 