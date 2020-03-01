import re

with open('test_subtitle1.srt', 'r') as f:
    subtitles = f.read()
    
num_pat = r'(\d+)'
time_pat = r'(\d{2,}:\d{2}:\d{2},\d{3}) --> (\d{2,}:\d{2}:\d{2},\d{3})'
sentence_pat = r'([^\n]*)\n'

data_pattern = re.compile(r'\n'.join([num_pat, time_pat, sentence_pat]))

sentences = []

for i in re.finditer(data_pattern, subtitles):
    sentences.append(i.group(4))

with open('test_subtitle.txt', 'w') as f:
    for item in sentences:
        f.write(item + ' ')
