from rest_framework import serializers 
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tweet 
		fields = ('id', 'content', 'created_date', 'user')
		read_only_fields = ('created_date', 'user')

