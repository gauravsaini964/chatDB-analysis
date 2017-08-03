from collections import Counter
import pprint
x = raw_input('Enter filename with extension.')



# with open(x) as f:
#     lines = f.read().splitlines()
#     # lines = [line.rstrip('\n') for line in open('filename')]
#     # print lines
#
# print lines.count()

def total_question_asked():
    question_mark = {'?'}
    question_count = 0
    chat_dict = {}
    with open(x, 'r') as f:
        for line in f:
            splitLine = line.split()
            question_count = Counter(c for line in f for c in line if c in question_mark)

    print 'Total question asked in this chat: %s' % (question_count.values())


def most_talkative():


total_question_asked()