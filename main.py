import webbrowser
import time
import random
import subprocess

url=["https://www.google.com/","https://www.facebook.com/","https://www.youtube.com/"]

chrome_path=r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe'

webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(chrome_path))

start_time = time.time()

hour = 24

seconds = 60

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    index = 0
    webbrowser.get('chrome').open(url[index])

    sleeptime = random.randint(30, 60)
    print(url[index])
    print("\n" + str(sleeptime))
    time.sleep(sleeptime)

    subprocess.call("c:\\windows\\system32\\taskkill.exe /im chrome.exe /f", shell=True)

    if elapsed_time > seconds:
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        subprocess.call(["shutdown", "-f", "-s", "-t", "1"])
        break