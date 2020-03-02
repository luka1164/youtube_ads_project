from pytube import YouTube

video_url = str(input())

video = YouTube(video_url)

# print(video.captions.all())

subs = video.captions.get_by_language_code('en')

subs_srt = subs.generate_srt_captions()

with open(video_url+'_subs.srt', 'w') as file:
    file.write(subs_srt)

