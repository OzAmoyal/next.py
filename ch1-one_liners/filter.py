def filter_song(file):
    return file.endswith('.mp3')

def use_filter():
    file_list=['resume.pdf','Bohemian Raphsody.mp3','Rondelim.mp3','helloworld.java']
    song_list=filter(filter_song,file_list)
    print(list(song_list))

use_filter()