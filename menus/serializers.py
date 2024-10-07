from rest_framework import serializers
from .models import Menu, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода иерархического списка меню"""
    children = serializers.SerializerMethodField()
    url_resolved = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'url_resolved', 'children']

    def get_children(self, obj):
        queryset = obj.children.order_by('order')
        serializer = MenuItemSerializer(queryset, many=True)
        return serializer.data

    def get_url_resolved(self, obj):
        return obj.get_absolute_url()


class MenuSerializer(serializers.ModelSerializer):
    """Сериализатор для пунктов меню"""
    items = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'name', 'items']

    def get_items(self, obj):
        root_items = obj.items.filter(parent__isnull=True).order_by('order')
        serializer = MenuItemSerializer(root_items, many=True)
        return serializer.data
