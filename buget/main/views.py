from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import *
from .models import *
from django.http import JsonResponse
import schedule
import schedule
import time
import datetime

def update_payed():
    obj = Plans.objects.all()
    if obj:
        obj.update(payed=False)
        print('boldi')
    else:
        print('bomadi')
    return True

class HomeView(View):

    def get(self, request):
        schedule.every(1).seconds.do(update_payed)

        while True:
            if datetime.datetime.now().strftime('%H,%M') == '15,18':
                schedule.run_pending()
            else:
                break

        form = AddPlan(request.GET)
        plans = Plans.objects.all().order_by('-id')
        buget = MyBuget.objects.last()
        context = {
            'buget':buget,
            'form':form,
            'plans':plans,
        }
        return render(request, 'home.html', context)

    def post(self, request):
        form = AddPlan(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AddPlan()
        context = {
            'form':form,
        }
        return render(request, 'home.html', context)


class PlansUpdate(UpdateView):
    model = Plans
    form_class = AddPlan
    success_url = '/'
    template_name = 'update.html'

class PlansDelete(DeleteView):
    model = Plans
    success_url = '/'
    template_name = 'delete.html'

def pay(request, pk):
    plan = Plans.objects.get(pk=pk)
    buget = MyBuget.objects.last()
    if plan.payed == False:
        minus = buget.total - plan.spent
        buget.total = minus
        buget.spent += plan.spent
        buget.actions += 1
        buget.save()
        plan.payed = True
        plan.save()
        return redirect('/')
    else:
        return redirect('/')

