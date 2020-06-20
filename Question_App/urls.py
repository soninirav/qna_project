from django.urls import path
from .views import QuestionCreateView,QuestionUpdateView,QuestionDeleteView,MyQuestionListView,AnswerDeleteView,AnswerUpdateView
from . import views
urlpatterns=[
    path('',views.index,name='home'),
    path('question/create/',QuestionCreateView.as_view(),name='question-create'),
    path('question/<int:pk>/update/',QuestionUpdateView.as_view(),name='question-update'),
    path('answer/<int:pk>/update/',AnswerUpdateView.as_view(),name='answer-update'),
    path('question/<int:pk>/delete/',QuestionDeleteView.as_view(),name='question-delete'),
    path('answer/<int:pk>/delete/',AnswerDeleteView.as_view(),name='answer-delete'),
    #working path('question/<int:pk>/answer/',views.AnswerListView,name='question-detail'),
    path('question/myquestion/',MyQuestionListView.as_view(),name='my-question'),
    path('myanswer/',views.MyAnswerListView,name='my-answer'),
    path('question/<int:pk>/answer/',views.AnswerCreateDetailView,name='question-detail'),
    #path('question/<int:pk>/answer/',AnswerListView.as_view(),name='question-detail'),
    #path('question/<int:pk>/giveanswer/',AnswerCreateView.as_view(),name='question-detail'),

]
