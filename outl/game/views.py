# bot/views.py
from django.shortcuts import render
from .forms import UserDataForm

from random  import randint

def index(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            user_data = form.save()
            prank_sentences = [
                    "Surprise! You’ve just been pranked by your very own data-hungry ghost!",
                    "Congratulations! You’ve unlocked the ultimate prank: no personal AI, just silly fun!",
                    "Oops! Looks like your personal AI is just a figment of your imagination!",
                    "You’ve been bamboozled! This ‘AI’ is as real as a unicorn!",
                    "Gotcha! Your personal assistant is just me, having a laugh!",
                    "Guess what? There’s no personal AI, just a playful prankster behind the screen!",
                    "You thought you’d get a personal AI? Nope! Just a prank on repeat!",
                    "Surprise! You’ve just been the star of the greatest prank show ever!",
                    "Womp womp! Your data went straight to the land of useless pranks!",
                    "Ha! Your personal AI was just an elaborate joke—hope you enjoyed the ride!"
                        ]
            i=randint(0,9)
            prank=prank_sentences[i]
            prank={"prank":prank,"len":len(prank)}



            return render(request, 'reveal.html', {'data': user_data,"prank":prank})
    else:
        form = UserDataForm()
    return render(request, 'index.html', {'form': form})
def loading(request):
    if request.method =='GET':
        return render(request, 'loading.html')
    
    
def homepage(request) :
    if request.method == 'GET' :
        return render(request,'homepage.html') 