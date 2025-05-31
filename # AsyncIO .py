import asyncio
import requests

def download1():
    url = "https://c4.wallpaperflare.com/wallpaper/780/341/142/anime-sharingan-red-eyes-naruto-shippuuden-wallpaper-preview.jpg"
    r = requests.get(url, allow_redirects=True)
    filename="Py1down.jpg"
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(f"Downloaded: {filename}")
def download2():
    url="https://c4.wallpaperflare.com/wallpaper/840/954/346/dark-night-rain-car-wallpaper-preview.jpg"
    r=requests.get(url,allow_redirects=True)
    filename="Py2down.jpg"
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(f"Downloaded: {filename}")
def download3():
    url="https://c4.wallpaperflare.com/wallpaper/440/217/250/skull-and-bones-2018-video-game-wallpaper-preview.jpg"
    r=requests.get(url,allow_redirects=True)
    filename="Py3down.jpg"
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(f"Downloaded: {filename}")
async def main():
    task1=asyncio.to_thread(download1)
    task2=asyncio.to_thread(download2)
    task3=asyncio.to_thread(download3)
    await asyncio.gather(task1,task2,task3)

asyncio.run(main())