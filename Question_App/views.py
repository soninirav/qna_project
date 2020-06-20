from django.shortcuts import render,redirect
from .models import Question,Answer
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AnswerForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
import datetime

#from collections import OrderedDict
#from django.views.generic import View
#from .forms import QuestionCreationForm
# Create your views here.


def index(request):
    context={
        'q_list':Question.objects.all().order_by('-created_time'),
        'A_list':Answer.objects.all(),
        
    }
    return render(request,'ui/index.html',context)



class MyQuestionListView(ListView):
    model=Question
    template_name='ui/my_question_list.html'
    context_object_name='q_list'
    ordering=['-created_time']


def MyAnswerListView(request):
    #dict=OrderedDict()


    uid=request.user.id
    my_question_list=[]
    my_answer_list=[]
    main_list=[]
    answer_of_loggedin_user=Answer.objects.all().filter(user_id=uid)# asnwers by loggedin user
    for i in answer_of_loggedin_user:
         id_of_selected_question=Answer.objects.values('selected_question').filter(answer=i)[0]['selected_question']#question id by logged in user
         question_for_answer=Question.objects.values('question').filter(id=id_of_selected_question)[0]['question'] #finds a question for given answer by logged in user
         #dict[question_for_answer]=i
         my_question_list.append(question_for_answer)  #my questions list
         my_answer_list.append(i) #my answer list

    for a in range(len(my_question_list)):
        for b in range(len(my_answer_list)):
            if a==b:
                k=[]
                k.append(my_question_list[a])
                k.append(my_answer_list[b])
                main_list.append(k)
                break

    context={
        'my_answer_list':main_list,
        'title':'| My Answers'
    }
    return render(request,'ui/my_answer_list.html',context)




def AnswerCreateDetailView(request,pk):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            a=form.save(commit=False)
            a.user=request.user
            a.selected_question=Question.objects.get(id=pk)
            a.save()
            form=AnswerForm()

            messages.success(request,'Your Answer Posted Succesfully ! ')
            #return redirect('question-detail')
    else:
        form = AnswerForm()
    context={
        'A_list':Answer.objects.all(),
        'A_list_filter':Answer.objects.filter(selected_question=pk).order_by('-answer_created_time'),#order by answer_created_time
        'question':Question.objects.values('question').filter(id=pk)[0]['question'], #wil give question from table according to
        #'reply_count':Answer.objects.all().filter(selected_question=pk).count(),
        'form':form,
        'title':'| Answers'
    }
    return render(request, 'ui/answer_detail.html', context)




class QuestionCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name='ui/question_create.html'
    #form_class=QuestionCreationForm
    model=Question
    fields=['title','question']
    success_url='/'
    success_message="Question Created Succesfully !"


    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class QuestionUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name='ui/question_create.html'
    model=Question
    fields=['title','question']

    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.info(self.request, 'Question Updated Succesfully !')
        return super().form_valid(form)

    def test_func(self):
        question=self.get_object()
        if self.request.user==question.user:
            return True
        return False

class QuestionDeleteView(LoginRequiredMixin,SuccessMessageMixin,UserPassesTestMixin,DeleteView):
    model=Question
    success_url='/'
    #success_message="Question Deleted Successfully !"
    template_name="ui/question_confirm_delete.html"
    #question_confirm_delete.html
    def test_func(self):
        question=self.get_object()
        if self.request.user==question.user:
            return True
        return False

class AnswerDeleteView(LoginRequiredMixin,SuccessMessageMixin,UserPassesTestMixin,DeleteView):
    model=Answer
    success_url='/'
    #success_message="Answer Deleted Successfully !"
    template_name='ui/answer_confirm_delete.html'

    def test_func(self):
        answer=self.get_object()
        if self.request.user==answer.user:
            return True
        return False

class AnswerUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name='ui/answer_detail.html'
    model=Answer
    fields=['answer']

    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.info(self.request, 'Answer Updated Succesfully !')
        return super().form_valid(form)

    def test_func(self):
        answer=self.get_object()
        if self.request.user==answer.user:
            return True
        return False
