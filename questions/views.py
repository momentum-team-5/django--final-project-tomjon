from django.shortcuts import render, redirect, get_list_or_404
from django.core.mail import send_mail, mail_admins
from django.contrib.messages import success, error
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

def questions_list(request):
    questions = Question.objects.all()
    return render(request, "questions_list.html", {"questions": questions})

def questions_detail(request, pk):
    question = get_list_or_404(Question, pk=pk)
    answer = question.answer
    if request.method =="GET":
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            success(request, "Answer saved!")
            return redirect(to="questions_detail", pk=question.pk)
        else:
            error(request, "Couldn't save answer")
    return render(request, "questions_detail.html", {"question": question, "answer": answer, "form": form})

@login_required
def add_question(request):
    if request.method == "GET":
        form = QuestionForm()

    else:
        form = QuestionForm(data=request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user # associate the new poem with the currently signed in user
            question.save()
 
            success(request, "Your question was created!")

            return redirect(to="questions_list")

        else:
            error(request, "Your question could not be created")

    return render(request, "questions_add.html", {"form": form})

@login_required
def questions_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    success(request, "Your question was deleted. Hope you got the answer you wanted.")

    return redirect(to="questions_list")    

def add_favorite(request, pk, user_pk):
    question = get_object_or_404(Question, pk=pk)
    user = get_object_or_404(User, pk=user_pk)
    if question.favorites.filter(pk=user_pk).count() == 0:
        question.favorites.add(user)
        success(request, "Favorite added :)")
    return redirect(to="questions_list")
    # need to be able to favorite answers as well
    # repeat entire code block or just add answer = get_obj... +