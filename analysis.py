from collections import Counter, defaultdict
from fileparser import NAME_MSG, MSG_ONLY, x ,name_msg_filgen, message_only_filegen
from wordcloud import WordCloud
import matplotlib.pyplot as plot
import requests
from pprint import pprint as pp
from termcolor import colored

# generate files
name_msg_filgen(x)
message_only_filegen(x)

Students = []
MESSAGE_DICT = []
d = defaultdict(list)


def total_question_asked():
    question_mark = {'?'}
    question_count = 0
    chat_dict = {}
    with open(x, 'r') as f:
        for line in f:
            question_count = Counter(c for line in f for c in line if c in question_mark)

    print colored('Total question asked in this chat: %s', 'cyan', attrs=['bold']) %(question_count.values())


def most_talkative(filename):
    k,v = 0,0
    with open(filename) as f:
        for line in f:
            if ":" in line:
                #splits element when it encounters :
                k, v = line.rstrip().split(":")
                d[k].extend(map(str.strip, v.split(",")) if v.strip() else [])
            else:
                d[k].append(line.rstrip())

            Students.append(d.keys())

        # msg_record = []
        # key_field = key
        # value_field = str(len([item for item in value]))
        # fields = key_field + value_field
        # msg_record.append(fields)
        # for i in msg_record.values():
    print colored("Total Student present in today's chat : %d", 'cyan', attrs=['bold']) %(len(d.keys()))
    print colored('Students Present along with their no of message :', 'white', attrs=['bold'])
    for key, value in d.items():
        print (key, len([item for item in value]))


def analyze_Sentiment(filename):
    # parse each statement in paralleldots
    # store result in list
    # count positive and negative
    # show whichever is max
    positivity = 0
    negativity = 0
    with open(filename) as f:
        data = f.read().splitlines()
        print colored('Analyzing./', 'white', attrs=['bold'])
        print colored('This might take time according to file size', 'red', attrs=['bold'])
        print colored('Analyzing./', 'white', attrs=['bold'])
        
        for line in range(0,len(data)):
            sentence = data[line]
            API_KEY = 'QcnFyRDYtKrD6Bz68BuKxE8wcCmtBd7cc7DBfJxDf2s'
            request_url = ('https://apis.paralleldots.com/sentiment?sentence1=%s&apikey=%s') % (sentence, API_KEY)
            result = requests.get(request_url).json()
            if result['sentiment'] >= 0.600000:
                positivity = positivity + 1
            elif result['sentiment'] < 0.600000:
                 negativity = negativity + 1
    if positivity > negativity:
        print colored("Overall nature of meeting today was : Positive" , 'cyan' ,attrs=['bold'])
    else:
        print colored("Overall nature of meeting today was : Positive", 'cyan', attrs=['bold'])


def generate_wordcloud(filename):
    with open(filename) as f:
        data = f.read()

    wordcloud = WordCloud(background_color='white',
                          width=1080,
                          height=1920).generate(data)
    plot.figure()
    plot.imshow(wordcloud, interpolation="bilinear")
    plot.axis("off")
    plot.savefig('cloud.png')
    flag = False



analyze_Sentiment(MSG_ONLY)
total_question_asked()
most_talkative(NAME_MSG)
generate_wordcloud(MSG_ONLY)
