from .models import Question,Answer

def trending_question_context(request):
    list_of_question_count=[]
    list_of_trending_questions=[]
    for i in Question.objects.values('id'):
         list_of_question_count.append(Answer.objects.filter(selected_question=i['id']).count())
    list_of_question_count.sort()
    for top_que_count in list_of_question_count[-1::-1]:
        for i in Question.objects.values('id'):
            if Answer.objects.filter(selected_question=i['id']).count()==top_que_count:
                temp=[]
                temp.append(i['id']) #id of question
                temp.append(Question.objects.values('question').filter(id=i['id'])[0]['question'])
                temp.append(Answer.objects.values('answer').filter(selected_question=i['id']).count())
                if temp[0] not in [l[0] for l in list_of_trending_questions]:
                    list_of_trending_questions.append(temp)
                    #print('id=',temp[0])
                    #print('Q=',temp[1])
                    #print('count=',top_que_count)
                    




    return {
        'trending_question':list_of_trending_questions[:5] #only 5 question
    }
