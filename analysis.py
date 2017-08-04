from collections import Counter
import pprint
from fileparser import NAME_MSG, MSG_ONLY, x ,name_msg_filgen, message_only_filegen

pp = pprint.PrettyPrinter(indent=4)
# generate files
name_msg_filgen(x)
message_only_filegen(x)

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

def createDictionary(filename):
  file = open(filename)
  contents = file.read()
  print contents,"\n"
  # data_list = [lines.split(",") for lines in contents.split("\n")]
  # for line in data_list:
  #   regNumber = line[0]
  #   name = line[1]
  #   phoneExtn = line[2]
  #   carpark = line[3].strip()
  #   details = (name,phoneExtn,carpark)
  #   data_dict[regNumber] = details
  # print data_dict,"\n"
  # print data_dict.items(),"\n"
  # print data_dict.values()
  #

createDictionary(NAME_MSG)