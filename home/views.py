from django.views.generic.base import TemplateView
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.views import View
from .models import *


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context

    def post(self,request,*args,**kwargs):
        context = self.get_context_data()
        username = request.POST.get('username')
        option = request.POST.get('option')
        room_code = request.POST.get('room_code')

        if option =='1':
            game = Game.objects.filter(room_code=room_code).first()
            if game is None:
                messages.success(request,"Room code not found")
                return HttpResponseRedirect('/')
            if game.is_over:
                messages.success(request,"Game is over")
                return HttpResponseRedirect('/')

            game.game_opponent = username
            game.save()
        else :
            game = Game(game_creator=username,room_code =room_code)
            game.save()
        
        return HttpResponseRedirect('/play/'+room_code+'?username='+username)

        # return super(TemplateView, self).render_to_response(context)
        
        

class Play(TemplateView):
    template_name = 'play.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get(self, request, *args, **kwargs) :
        context = self.get_context_data()
        username = request.GET.get('username')
        room_code = kwargs.get('room_code')
        context["room_code"] = room_code
        context["username"] = username
        return super(TemplateView, self).render_to_response(context)