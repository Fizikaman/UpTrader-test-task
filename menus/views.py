from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Menu
from .serializers import MenuSerializer


class MenuViewSet(viewsets.ViewSet):
    """Вьюха для вывода иерархического меню"""

    def retrieve(self, request, pk=None):
        try:
            menu = Menu.objects.get(name=pk)
        except Menu.DoesNotExist:
            return Response({'detail': 'Menu not found.'}, status=404)

        serializer = MenuSerializer(menu, context={'request': request})

        return render(request, 'base.html', {'menu': serializer.data})
