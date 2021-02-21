import threading
import multiprocessing
import time
import datetime

class Song:
    def __init__(self, duration, name):
        self.duration = duration
        self.name = name
        self.streaming_count = 0

    def play(self, username):
        print(f'Start play {self.name}')
        print(datetime.datetime.now())
        self.songplays = SongPlays(self, username)
        self.songplays.thread = threading.Thread(target=self._play)
        self.songplays.thread.start()


    def _play(self):
        print(f'Start _play for {self.name}')
        time.sleep(self.duration)
        self.stop(form_thread=True)
        print(f'End _play for {self.name}')


    def stop(self, form_thread=False):
        if not form_thread:
            self.songplays.thread._is_stopped = True
        print(datetime.datetime.now())
        print(f'Duration of {self.name} play {time.time()-self.songplays.startime}')



class SongPlays:
    def __init__(self, song, username):
        self.song = song
        self.username = username
        self.startime = time.time()


def fuctorial(n):
    if n == 1:
        return 1
    return n * fuctorial(n-1)



process_1 = multiprocessing.Process(target=fuctorial, args=(13,))
process_1 = multiprocessing.Process(target=fuctorial, args=(12,))

def thread_timing():
    print('Threading')
    thread_1 = threading.Thread(target=fuctorial, args=(13,))
    thread_2 = threading.Thread(target=fuctorial, args=(12,))
    thread_4 = threading.Thread(target=fuctorial, args=(12,))
    thread_3 = threading.Thread(target=fuctorial, args=(12,))
    start_time = time.time()
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_2.join()
    thread_1.join()
    thread_3.join()
    thread_4.join()
    print(time.time()-start_time)

def process_timing():
    print('Processing')
    process_1 = multiprocessing.Process(target=fuctorial, args=(13,))
    process_2 = multiprocessing.Process(target=fuctorial, args=(12,))
    process_3 = multiprocessing.Process(target=fuctorial, args=(12,))
    process_4 = multiprocessing.Process(target=fuctorial, args=(12,))
    start_time = time.time()
    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()
    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()
    print(time.time()-start_time)



if __name__ == '__main__':
    thread_timing()
    process_timing()
    # song_1 = Song(12, 'Song_1')
    # song_2 = Song(5, 'Song_2')
    # song_2.play('User_1')
    # song_1.play('User_1')
    # time.sleep(7)
    # song_1.stop()


