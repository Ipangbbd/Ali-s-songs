import time
from threading import Thread, Lock
import sys

lock = Lock()


def animate_text(text, delay: float = 0.1) -> None:
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()


def sing_lyrics(lyrics_line: str, delay_seconds: float = 0.1, char_speed: float = 0.06) -> None:
    time.sleep(delay_seconds)
    animate_text(lyrics_line, char_speed)


def sing_song() -> None:
    lyrics = [
        ('Come on, come on, come on', 0.11),
        ('Come on, come on, come on', 0.11),
        ('Number one party anthem', 0.2),
        ('Come on, come on, come on', 0.2),
        ("Before the moment's gone", 0.15),
        ('Number one party anthem, yeah, yeah', 0.2),
        ('The look of love, the rush of blood', 0.16),
        ("The \"She's with me\" is the Gallic shrug", 0.09),
        ('The shutterbugs, the Camera Plus', 0.12),
        ('The black and white and the color dodge', 0.1),
        ('The good time girls, the cubicles', 0.15),
        ('The house of fun, the number one', 0.18),
        ('Party anthem, oh', 0.3),
    ]

    # Stagger the start times so lines enter in sequence
    delays = [i * 3.3 for i in range(len(lyrics))]

    threads = []
    for i, (line, speed) in enumerate(lyrics):
        line_delay = delays[i] if i < len(delays) else (delays[-1] if delays else 0.0)
        t = Thread(target=sing_lyrics, args=(line, line_delay, speed))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    sing_song()


