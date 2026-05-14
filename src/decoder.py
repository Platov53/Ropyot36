import numpy as np
import pyaudio
from PIL import Image

WIDTH, HEIGHT = 320, 240
RATE = 44100
CHUNK = 512

def decoder_sstv():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

    img = Image.new('RGB', (WIDTH, HEIGHT), "black")
    pixels = img.load()

    x, y = 0, 0
    print("Aguardando sinal SSTV...")

    try:
        while y < HEIGHT:
            data = stream.read(CHUNK, exception_on_overflow=False)
            samples = np.frombuffer(data, dtype=np.int16)

            fft_result = np.fft.rfft(samples)
            freqs = np.fft.rfftfreq(len(samples), 1/RATE)
            
            freq_dominante = freqs[np.argmax(np.abs(fft_result))]

            if 1150 <= freq_dominante <= 1250:
                x = 0
                y += 1
                continue 

            if 1500 <= freq_dominante <= 2300:
                brilho = int((freq_dominante - 1500) * 255 / (2300 - 1500))
                
                if x < WIDTH and y < HEIGHT:
                    pixels[x, y] = (brilho, brilho, brilho)
                    x += 1

        img.show()
        img.save("audios-saida/captura_robot36.png")

    except KeyboardInterrupt:
        pass
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

#Ainda esta com alguns erros, e muito cru, em breve acertarei tudo. :)