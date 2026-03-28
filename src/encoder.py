import os
import webbrowser
import Ropyot36
from PIL import Image
from pysstv.color import Robot36

def encoder():
    base = os.path.dirname(os.path.abspath(__file__))
    fotos = os.path.join(base, "img")
    audios = os.path.join(base, "audios-saida")
    
    if not os.path.exists(fotos):
        os.makedirs(fotos)
        print("Pasta criada de imagens criada!")
        return

    extensao = ("jpg", "jpeg", "png")
    arquivos = [f for f in os.listdir(fotos) if f.lower().endswith(extensao)]
    if not arquivos:
        print("Não há arquivos, por favor coloque na pasta img")
    clear()
    print("""
>>======================================<<
|| _____                    _           ||
|||  ___|                  | |          ||
||| |__ _ __   ___ ___   __| | ___ _ __ ||
|||  __| '_ \ / __/ _ \ / _` |/ _ \ '__|||
||| |__| | | | (_| (_) | (_| |  __/ |   ||
||\____/_| |_|\___\___/ \__,_|\___|_|   ||
>>======================================<<                                 
""")
    for i, arquivo in enumerate(arquivos):
        print(f"[{i}] {arquivo}")
    print("[V] Voltar")
    print(">>======================================<<")

    while True:
        try:
            
            selecao = input("Digite o número da imagem: ").lower()
            if selecao == "v":
                Ropyot36.menu()
            imagem = arquivos[int(selecao)]
            break
        except (ValueError, IndexError):
            print("Error: Escolha uma das opções na lista.")

    caminho_imagem = os.path.join(fotos, imagem)
    nome_audio = imagem.rsplit('.',1)[0] + ".wav"
    caminho_audio = os.path.join(audios, nome_audio)
    if not os.path.exists(audios):
        os.makedirs(audios)
    
    try:
        img = Image.open(caminho_imagem).resize((320, 240), Image.Resampling.LANCZOS)
        robot_sstv = Robot36(img, 44100, 16)
        with open(caminho_audio, "wb") as f:
            robot_sstv.write_wav(f)
        print("Audio gerado")
        play_resp = input("Play [S/N]: ").lower()
        caminho_play_audio = os.path.abspath(caminho_audio)
        if play_resp == "s":
            webbrowser.open(caminho_play_audio)
    except Exception as e:
        print(f"Error: {e}")


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')