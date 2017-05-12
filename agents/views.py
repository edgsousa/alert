import datetime

from django.contrib.auth import login
from rest_framework import status

from fcm_django.models import FCMDevice
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from social_django.utils import psa

from agents.models import Agent

class API(ViewSet):

    @permission_classes((IsAuthenticated,))
    def register_device(self, request):
        person = Agent.objects.get(user=request.user)
        regid = request.GET.get('registration_id')
        device_id, created = FCMDevice.objects.get_or_create(user=request.user, defaults={'type': 'android',
                                                                                          'registration_id': regid})
        if created:
            person.device = device_id
            device_id.save()
            person.save()
        else:
            if device_id.user != person:
                return Response({'status': 'ERROR'})
        return Response({'status': 'OK'})

    def register(self, request, backend):
        return API.__register_impl__(request, backend)

    @permission_classes((IsAuthenticated))
    def location(self, request):
        agent = Agent.objects.get(user=request.user)
        if request.method == 'GET':
            return Response({
                'timestamp': agent.pos_timestamp,
                'longitude': agent.pos_longitude,
                'latitude': agent.pos_latitude})
        elif request.method == 'POST':
            try:
                long = float(request.data.get('longitude'))
                lat = float(request.data.get('latitude'))
                speed = float(request.data.get('speed'))
                bearing = float(request.data.get('bearing'))
                timestamp = datetime.datetime.now()
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=e.args)
            agent.pos_longitude = long
            agent.pos_timestamp = timestamp
            agent.pos_latitude = lat
            agent.pos_speed = speed
            agent.pos_bearing = bearing
            agent.save()
            return Response({'status': 'OK',
                             'timestamp': agent.pos_timestamp,
                             'longitude': agent.pos_longitude,
                             'latitude': agent.pos_latitude,
                             'speed': agent.pos_speed,
                             'bearing': agent.pos_bearing})

    @staticmethod
    @psa('social:complete')
    def __register_impl__(request, backend):
        # This view expects an access_token GET parameter, if it's needed,
        # request.backend and request.strategy will be loaded with the current
        # backend and strategy.
        try:
            user = request.backend.do_auth(request.GET.get('access_token'))
            if user:
                login(request, user)
                newuser, created = Agent.objects.get_or_create(user=user)
                if created:
                    newuser.save()
                return Response(user.username)
        except Exception as e:
            return Response(status=HttpResponseBadRequest.status_code, data=e.args)

