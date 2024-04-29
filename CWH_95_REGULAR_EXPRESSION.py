import re

pattern = "[A-Z]yasa"
text = '''
According to what one figure says at Mbh. 1.1.50, there were three versions of the epic, beginning with Manu
(1.1.27), Astika (1.3, sub-Parva 5), or Vasu (1.57), respectively. These versions would correspond to the
addition of one and then another 'frame' settings of dialogues. The Vasu version would omit the frame settings
and begin with the account of the birth of Vyasa. The astika version would add the sarpasattra and ashvamedha 
material from Brahmanical literature, introduce the name Mahābhārata, and identify Vyasa as the work's author.
The redactors of these additions were probably Pancharatrin scholars who according to Oberlies (1998) likely
retained control over the text until its final redaction. Mention of the Huna in the Bhishma Parva however
appears to imply that this Parva may have been edited around the 4th century.
'''
#
# match = re.search(pattern,text)
# print(match)

match = re.finditer(pattern,text)

for matches in match:
    print(matches.span())