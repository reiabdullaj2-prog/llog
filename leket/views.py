from datetime import datetime
from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum
from .models import fitimet, shpenzimet, totali
from .forms import fitimetForm, shpenzimetForm
def shtepia(request):
    fitimet_totale = fitimet.objects.aggregate(Sum('shuma'))['shuma__sum'] or 0
    shpenzimet_totale = shpenzimet.objects.aggregate(Sum('shuma'))['shuma__sum'] or 0
    gjendja = fitimet_totale - shpenzimet_totale
    totali.objects.update_or_create(id=1, defaults={'fitimet_totale': fitimet_totale, 'shpenzimet_totale': shpenzimet_totale, 'gjendja': gjendja})
    return render(request, 'blog/shtepia.html', {'fitimet_totale': fitimet_totale, 'shpenzimet_totale': shpenzimet_totale, 'gjendja': gjendja})
def fitimet_list(request):
    fitimet_list = fitimet.objects.all()
    total=fitimet_list.aggregate(Sum('shuma'))['shuma__sum'] or 0
    return render(request, 'blog/fitimet_list.html', {'fitimet_list': fitimet_list})
class krijoardhuraCreateView(CreateView):
    model=fitimet
    form_class=fitimetForm
    template_name='blog/krijo_ardhura.html'
    success_url=reverse_lazy('fitimet_list')
class redaktoardhuraUpdateView(UpdateView):
    model = fitimet
    form_class = fitimetForm
    template_name = 'blog/redakto_ardhura.html'
    success_url = reverse_lazy('fitimet_list')
class fshiardhuraDeleteView(DeleteView):        
    model = fitimet
    template_name = 'blog/fshi_ardhura.html'
    success_url = reverse_lazy('fitimet_list')

def shpenzimet_list(request):
    shpenzimet_list = shpenzimet.objects.all()
    total=shpenzimet_list.aggregate(Sum('shuma'))['shuma__sum'] or 0
    return render(request, 'blog/shpenzimet_list.html', {'shpenzimet_list': shpenzimet_list, 'total': total})
class KrijoShpenzimeCreateView(CreateView):
    model = shpenzimet
    form_class = shpenzimetForm
    template_name = 'blog/krijo_shpenzime.html'
    success_url = reverse_lazy('shpenzimet_list')
class RedaktoShpenzimeUpdateView(UpdateView):
    model = shpenzimet
    form_class = shpenzimetForm
    template_name = 'blog/redakto_shpenzime.html'
    success_url = reverse_lazy('shpenzimet_list')
class FshiShpenzimeDeleteView(DeleteView):
    model = shpenzimet
    template_name = 'blog/fshi_shpenzime.html'
    success_url = reverse_lazy('shpenzimet_list')
def statistikat(request):
    viti = request.GET.get('viti')
    
    # Krijoji variablat me vlerë fillestare 0 përpara se të fillosh çdo gjë
    fitimet_totale = 0
    shpenzimet_totale = 0
    
    if viti:
        # Nëse ka vit të zgjedhur
        viti = int(viti)
        fitimet_totale = fitimet.objects.filter(data__year=viti).aggregate(Sum('shuma'))['shuma__sum'] or 0
        shpenzimet_totale = shpenzimet.objects.filter(data__year=viti).aggregate(Sum('shuma'))['shuma__sum'] or 0
    else:
        # Nëse nuk ka vit, merr totalin e përgjithshëm
        fitimet_totale = fitimet.objects.aggregate(Sum('shuma'))['shuma__sum'] or 0
        shpenzimet_totale = shpenzimet.objects.aggregate(Sum('shuma'))['shuma__sum'] or 0

    # Tani gjendja do të funksionojë gjithmonë sepse variablat janë deklaruar lart
    gjendja = fitimet_totale - shpenzimet_totale
    
    context = {
        'viti': viti,
        'fitimet_totale': fitimet_totale,
        'shpenzimet_totale': shpenzimet_totale,
        'gjendja': gjendja,
        'vitet': [2025, 2026, 2027]
    }
    return render(request, 'blog/statistikat.html', context)
                                                             