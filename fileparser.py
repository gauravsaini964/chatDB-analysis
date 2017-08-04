import re

x = raw_input('Enter filename with extension')
NAME_MSG = 'name-msg.txt'
MSG_ONLY = 'msg-only.txt'

##Generate log file in name:message format
# Strip emoticons

def name_msg_filgen(filename):
	b = open(filename, "r")
	a = open(NAME_MSG, "w")
	y = b.readline().decode('utf-8-sig').encode('utf-8')
	while y:
		if (y != '\r\n'):
			temp = y.split("From ", 1)
			x = temp[1]
			emoticon = {':P',':X',':x',':p',':d',':)',':(',':D',':v','1:00','2:00','3:00','4:00','5:00','6:00','7:00'
				,'8:00','9:00','10:00','11:00','12:00'}
			for y in emoticon:
				x = x.replace(y,'emoticon')
			# x = re.sub('[?\.#_]','',x)
			# x = re.sub('[\s]+',' ',x)
			a.write(x)
		y = b.readline()


# Generate message only log file to generate wordcloud and analytics
def message_only_filegen(filename):
	c = open(filename, "r")
	d = open(MSG_ONLY, "w")
	y = c.readline().decode('utf-8-sig').encode('utf-8')
	while y:
		if (y != '\r\n'):
			temp = y.split(": ", 1)
			x = temp[1]
			# Handle emoticons coz breaking dictionary generator and time too
			emoticon = {':P',':X',':x',':p',':d',':)',':(',':D',':v','1:00','2:00','3:00','4:00','5:00','6:00','7:00'
				,'8:00','9:00','10:00','11:00','12:00'}
			for y in emoticon:
				x = x.replace(y,'emoticon')
			# x = re.sub('([\\;][\)\|\\\/dDOoPp\(\\][\(\)DOo]?)','',x)
			# # x = re.sub('[?\.#_]','',x)
			# # x = re.sub('[\s]+',' ',x)
			d.write(x)
		y = c.readline()

# + "\n"