from rest_framework.decorators import list_route, permission_classes, detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
import datetime

class ServerStatus(ViewSet):

    @permission_classes((IsAuthenticated,))
    @list_route()
    def gettime(self, request):
        """
        Current UTC time of the server
        :param request:
        :return:
        """
        return Response(datetime.datetime.utcnow().isoformat())


