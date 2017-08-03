from collections import Counter
import pprint
x = raw_input('Enter filename with extension.')
# with open(x) as f:
#     lines = f.read().splitlines()
#     # lines = [line.rstrip('\n') for line in open('filename')]
#     # print lines
#
# print lines.count()
question_mark = {'?'}
question_count = 0
chat_dict = {}
with open(x, 'r') as f:
    for line in f:
        splitLine = line.split()
        chat_dict[(splitLine[0])] = " ".join(splitLine[1:])
        question_count = Counter(c for line in f for c in line if c in question_mark)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(chat_dict)

# count = Counter(chat_dict)
# pp.pprint(count)

# for i in chat_dict.values():
#     for j in range(0,len(chat_dict.values())):
#         if chat_dict.values() == "?":
#             question_count = question_count + 1

print 'Total question asked in this chat: %s' %(question_count.values())
