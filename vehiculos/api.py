from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.request import Request

from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Vehiculo
from .serializers import VehiculoSerializer


class VehiculoViewSet(viewsets.ViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def create(self, request:Request):

        serializer = VehiculoSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'data' : serializer.data
                },
                status= status.HTTP_200_OK
            )

        return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request:Request, pk = None):
        
        user_id = pk

        queryset = Vehiculo.objects.all().filter(user_id = user_id)
        vehiculos = get_list_or_404(queryset)
        serializer = VehiculoSerializer(instance = vehiculos, many = True)

        return Response(
            data = serializer.data,
            
            status = status.HTTP_200_OK
        )

    def update(self, request:Request, pk = None):

        serializer = VehiculoSerializer(data = request.data)

        if serializer.is_valid():
            
            vehiculo = Vehiculo.objects.get(id = pk)
            vehiculo.placas = serializer.data['placas']
            vehiculo.longitud = serializer.data['longitud']
            vehiculo.latitud = serializer.data['latitud']

            vehiculo.save()

            return Response(
                data = {
                    'data' : serializer.data
                },
                status = status.HTTP_202_ACCEPTED
            )
        
        return Response(
            serializer.errors, status = status.HTTP_400_BAD_REQUEST
        )
    
    def destroy(self, request:Request, pk = None):
        
        try:
            queryset = Vehiculo.objects.get(id = pk)
            queryset.delete()
            
            return Response(
                data = {
                    'data' : 'Se ha eliminado el vehiculo'
                },
                status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                data = {
                    'error' : str(e)
                },
                status = status.HTTP_409_CONFLICT
            )
