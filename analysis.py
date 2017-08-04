from collections import Counter, defaultdict
from pprint import pprint as pp
from fileparser import NAME_MSG, MSG_ONLY, x ,name_msg_filgen, message_only_filegen
import urllib
from wordcloud import WordCloud
import matplotlib.pyplot as plot

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

    print 'Total question asked in this chat: %s' % (question_count.values())


def most_talkative():
    chat_dict = {}
    temp_dict = {}
    #strip timestamp
    #make dict as key:value name:chat

    with open(x) as f:
        lines = f.readlines()
    with open(x, 'rb') as f:
        for line in f:
            splitLine = line.split()
            temp_dict[(splitLine[0])] = " ".join(splitLine[2:])
            # Dirty hack to remove timestamp
            temp_array = temp_dict.values()
            chat_dict = dict(s.split(':')[:2] for s in temp_array)

            ##Dekh yeh jo upar vala loop hai m.txt ke liye sirf 20 tak kaam kar rha hai
            #and x.txt ke liye direct show karta hai ki out of index
    #         mera topic hai ki text analysis like most talkative ?
    #  most question asked etc. abb isko name:chat ka key:value pair ban jaaye toh saaare
    #  saare operation asaan ho jayenge


    name_occurence_counter = Counter(chat_dict.keys())
    # pp.pprint(chat_dict)

# def createDictionary(filename):
#     data_dict = {}
#     file = open(filename)
#     contents = file.read()
#     # print contentsdata_list
#     data_list = [lines.split(",") for lines in contents.split("\n")]
#     # pp.pprint(data_list)
#     for line in data_list:
#         name = line[0]
#         message = line[0:]
#         details = (message)
#         data_dict[name] = details
#     pp.pprint(data_dict)
#     # print data_dict, "\n"
#     # print data_dict.items(), "\n"
#     # print data_dict.values()

def createDictionary(filename):
    k,v = 0,0
    with open(filename) as f:
        for line in f:
            if ":" in line:
                k, v = line.rstrip().split(":")
                d[k].extend(map(str.strip, v.split(",")) if v.strip() else [])
            else:
                d[k].append(line.rstrip())

            Students.append(d.keys())

    print "Total Student present in today's chat : %d" %(len(d.keys()))
    print 'Student present today : %s' %(d.keys())






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
    plot.show()


# createDictionary(NAME_MSG)

generate_wordcloud(MSG_ONLY)