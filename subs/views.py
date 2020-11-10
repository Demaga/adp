# from rest_framework import viewsets
# from rest_framework.response import Response

# from django.shortcuts import get_object_or_404

# from .serializers import SubSerializer
# from .models import Sub


# class SubViewSet(viewsets.ModelViewSet):
#     queryset = Sub.objects.all().order_by('name')
#     serializer_class = SubSerializer

#     def retrieve(self, request, pk=None):
#         queryset = Sub.objects.filter(name=pk)
#         contact = get_object_or_404(queryset, pk=1)
#         serializer = SubSerializer(contact)
#         return Response(serializer.data)


from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from subs.models import Sub
from subs.serializers import SubSerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def sub_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        subs = Sub.objects.all()
        serializer = SubSerializer(subs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def sub_detail(request, name):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        sub = Sub.objects.get(name=name)
    except Sub.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubSerializer(sub)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubSerializer(sub, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)