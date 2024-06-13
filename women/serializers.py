from rest_framework import serializers

from women.models import Women, TagPost


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagPost
        fields = ("tag",)


class WomenSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Women
        fields = ("title", "cat_id", "photo", "tags")
        depth = 1
