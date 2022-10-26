import webbrowser, time

url = input("URL do vídeo: ")
duration = input("Tempo de reprodução: ")

for i in range(5):
    webbrowser.open_new(url)
    time.sleep(int(duration))