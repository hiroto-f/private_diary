from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render

from django.views import generic
from .forms import InquiryForm, DiaryCreateForm
from .models import Diary
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

import logging
logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"
    

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self,form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
    
class DiaryListView(LoginRequiredMixin,generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries
    
class DiaryDetailView(LoginRequiredMixin,generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'

class DiaryCreateView(LoginRequiredMixin,generic.CreateView):
    
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.instance
        diary.user = self.request.user
        messages.success(self.request,'日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,'日記の作成に失敗しました。')
        return super().form_invalid(form)
    
class DiaryUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    fields = ['title','content','photo1','photo2','photo3']

    def get_success_url(self):
        #print(self.kwargs)
        return reverse_lazy('diary:diary_detail',kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request,'日記を更新しました')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '日記の更新に失敗しました')
        return super().form_invalid(form)
    