from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatbot', read_only=False,
              logic_adapters=[
                  {
                      'import_path':'chatterbot.logic.BestMatch',
                      'default_response':'Maaf, Klepond chatbot tidak mengetahui apa yang kamu maksud',
                      'maximun_similarity_threshold':0.90
                   }
                   ])

list_to_train = [

    "hai", #question
    "halo", #answer
    "siapa namamu?", 
    "aya Klepond Chatbot",
    "siapa yang paling tampan?",
    "ond Naravit Lertratkosum",
    "dimana klepond kerja?",
    "GMM",
    ""

]

ChatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)
ChatterbotCorpusTrainer.train('chatterbot.corpus.indonesia')
ChatterbotCorpusTrainer.train('chatterbot.corpus.english')


# def index(request):
#     return HttpResponse("this is my first url")

def index(request):
    return render(request, 'chat/index.html')

# def specific(request):
#     number= 97
#     return HttpResponse(number)

def specific(request):
    list1= [1,2,3,4,5,6,7,8,9,10]
    return HttpResponse(list1)

# def article(request, article_id):
#     return render(request, 'chat/index.html', {'article': article_id})


def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
