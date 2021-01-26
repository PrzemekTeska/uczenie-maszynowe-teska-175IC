# previous imports from synchronous version are maintained
import threading
from concurrent.futures import ThreadPoolExecutor
from imgurpython import ImgurClient

# Imgur client setup remains the same as in the synchronous version

# download_image() function remains the same as in the synchronous

client_secret = os.getenv("CLIENT_SECRET")
client_id = os.getenv("CLIENT_ID")

client = ImgurClient(client_id, client_secret)

def download_album(album_id):
    images = client.get_album_images(album_id)
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_image, images)

def main():
    download_album('PdA9Amq')

if __name__ == "__main__":
    print("Time taken to download images using multithreading: {}".format(timeit.Timer(main).timeit(number=1)))