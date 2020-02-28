import re

filename = r'test_subtitle.srt'
pattern_number = re.compile('^\d+$')
pattern_time = re.compile('^[\d]+:[\d]+:[\d]+,[\d]+ --> [\d]+:[\d]+:[\d]+,[\d]+$')
pattern_speech = re.compile("^[A-Za-z,;'\"\\s]+[.?!]*$")

for i, line in enumerate(open(filename)):
    for match in re.findall(pattern_number, line):
        print(match)

for i, line in enumerate(open(filename)):
    for match in re.findall(pattern_time, line):
        print(match)

for i, line in enumerate(open(filename)):
    for match in re.findall(pattern_speech, line):
        print(match)       

# ^\d+$
# ^[\d]+:[\d]+:[\d]+,[\d]+ --> [\d]+:[\d]+:[\d]+,[\d]+$
# ^[A-Za-z,;'\"\\s]+[.?!]*$
