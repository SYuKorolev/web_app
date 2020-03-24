#from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework import generics

from trend_app.models import Description
from .serializers import DescSerializer

#class DescView(APIView):
#    def get(self, request):
#        name = self.kwargs['name']
#        descs = Description.objects.filter(description__graph_name=name)
        # the many param informs the serializer that it will be serializing more than a single article.
#        serializer = DescSerializer(descs, many=True)
#        return Response({"articles": serializer.data})

class DescView(generics.ListAPIView):
    serializer_class = DescSerializer

    def get_queryset(self):
        queryset = Description.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(graph_name=name)
        return queryset