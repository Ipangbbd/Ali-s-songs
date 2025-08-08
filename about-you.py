import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyrics(lyrics, delay=0.1, speed=1):
    time.sleep(delay)
    animate_text(lyrics, speed)

def sing_song():
    lyrics = [
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten?", 0.1),
        ("About you", 0.1),
        ("There was something about you that now I can’t remember", 0.2),
        ("Is the same damn thing that makes my heart surrender", 0.1),
        ("And I miss you on a train and I miss you in the morning", 0.1),
        ("I never know what to think about...", 0.2)
        ("Think about youuuuuuuuuuuuuuuuuuuuu", 0.1)
    ]

    # Schedule offsets (seconds) for each lyric line. Length may differ from lyrics.
    delays = [0.1, 5.0, 20.0, 25.0, 25.0, 25.0, 27.0, 30.0]

    threads = []
    for i, (line, speed) in enumerate(lyrics):
        # If delays has fewer entries than lyrics, reuse the last delay; if empty, default to 0.0
        line_delay = delays[i] if i < len(delays) else (delays[-1] if delays else 0.0)
        t = Thread(target=sing_lyrics, args=(line, line_delay, speed))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    sing_song()