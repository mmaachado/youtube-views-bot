import webbrowser, time

# YouTube link to video
url = input("Video URL: ")
# How many time Python must watch the video
duration = input("Duration time: ")

# In range, determine how many time Python must open this video
for i in range(5):
    webbrowser.open_new(url)
    time.sleep(int(duration))