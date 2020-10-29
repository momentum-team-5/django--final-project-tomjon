from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, mail_admins
from django.contrib.messages import success, error
from users.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

def questions_list(request):
    questions = Question.objects.all()
    return render(request, "questions_list.html", {"questions": questions})

def questions_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
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
    return render(request, "questions_detail.html", {"question": question, "answers": answers, "form": form})

@login_required
def questions_add(request):
    if request.method == "GET":
        form = QuestionForm()
    else:
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
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

@login_required
def answers_add(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "GET":
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user 
            answer.save()
            success(request, "Your answer was submitted!")
            send_mail("Your question was answered", "Someone answered your question! Check it out.", recipient_list=[question.author.email], fail_silently=True)
            return redirect(to="questions_detail")
        else:
            error(request, "Your answer could not be submitted")
    return render(request, "questions_detail.html", {"form": form, "question": question})    


def add_favorite(request, pk):
    question = get_object_or_404(Question, pk=pk)
    user = request.user
    if user.is_authenticated:
        if question.favorites.filter(pk=user.pk).exists():
            message = "You can only favorite a question once."
        else:
            question.favorites.add(user)
            message =  "Favorite added"
    else:
        message = "Only signed in users can favorite questions" 
    numLikes = question.numfavorites()               
    return JsonResponse({"message": message, "numLikes": numLikes})
                    

def add_answer_favorite(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    user = request.user
    if user.is_authenticated:
        if answer.answer_favorites.filter(pk=user.pk).exists():
            message = "You can only favorite an answer once."
        else:
            answer.answer_favorites.add(user)
            message = "Favorite added!"
    else:
        message = "Only signed in users can favorite answers."
    numLikes = answer.numfavorites()           
    return JsonResponse({"message": message, "numLikes": numLikes})


def user_questions(request, pk):
    question_user = request.user
    question = question_user.questions.all()
    return render(request, "user_questions.html", {"questions": question, "question_user": question_user})

def mark_as_correct(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    user = request.user
    if user.is_authenticated and answer.question.author == user:
        answer.correct_answer = not answer.correct_answer
        answer.save()
        message = "Answer correctness changed"
    else:
        message = "Only the asker can mark answers as correct!"
    correct = answer.correct_answer           
    return JsonResponse({"message": message, "correct": correct})    

def correct_answers(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question_correct_answers = question.answers.filter(correct_answer=True)
    return render(request, "correct_answers.html", {"question": question, "question_correct_answers": question_correct_answers})
