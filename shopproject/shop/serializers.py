from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image_URL = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'size', 'currency', 'image_URL']

    def get_image_URL(self, products):
        request = self.context.get('request')
        image_URL = products.imageURL.url
        return request.build_absolute_uri(image_URL)
