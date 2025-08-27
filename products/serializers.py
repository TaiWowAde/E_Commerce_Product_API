from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id", "name", "description", "price", "stock_quantity", "image_url",
            "category", "created_by", "created_date", "updated_date"
        ]
        read_only_fields = ["id", "created_by", "created_date", "updated_date"]

    def create(self, validated_data):
        # auto-attach the logged-in user
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            validated_data["created_by"] = request.user
        return super().create(validated_data)
