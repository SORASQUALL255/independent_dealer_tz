from .models import DealerCenter, Vehicle
from .serializers import DealerCenterSerializer, VehicleSerializer
from .forms import DealerCenterForm, VehicleForm, LoginUserForm
from .permissions import IsOwner

from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

from rest_framework import permissions, renderers, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions



class DealerCenterList(generics.ListCreateAPIView):
    queryset = DealerCenter.objects.all()
    serializer_class = DealerCenterSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        d = self.request.user
        return DealerCenter.objects.filter(dealer=d)

class DealerCenterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DealerCenter.objects.all()
    serializer_class = DealerCenterSerializer
    permission_classes = [IsOwner]


class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        d = self.request.user
        return Vehicle.objects.filter(dealer=d)

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsOwner]


class DealerCenterFront(View):

    def get(self, request, *args, **kwargs):
        all_user = User.objects.all()
        try:
            all_dc = DealerCenter.objects.filter(dealer=request.user)
        except:
            all_dc = []
        all_veh = Vehicle.objects.all()
        new_dc = DealerCenterForm
        new_veh = VehicleForm
        cur_dealer = request.user

        return render(request, 'Dcenters/dcveh.html', context={
        'getdc': all_dc,
        'getveh': all_veh,
        'postdc': new_dc,
        'postveh': new_veh,
        'd': cur_dealer,
        'all_d': all_user
        })

    #def post(self, request):
    #    if request.method == "POST":
    #        form = DealerCenterForm(request.POST)
    #        post = form.save()
    #        post.save()
    #        return redirect('home')
    #    else:
    #        form = DealerCenterForm()
    #    return render(request, 'Dcenters/dcveh.html', {'postdc': form})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'Dcenters/login.html'

    def get_success_url(self):
        return reverse('home')


def logout_user(request):
    logout(request)
    return redirect('home')