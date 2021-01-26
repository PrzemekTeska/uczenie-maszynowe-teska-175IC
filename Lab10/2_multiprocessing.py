# previous imports from synchronous version remain
import multiprocessing
from imgurpython import ImgurClient

# Imgur client setup remains the same as in the synchronous version

# download_image() function remains the same as in the synchronous

client_secret = os.getenv("CLIENT_SECRET")
client_id = os.getenv("CLIENT_ID")

client = ImgurClient(client_id, client_secret)

def main():
    images = client.get_album_images('PdA9Amq')

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.map(download_image, [image.link for image in images])

if __name__ == "__main__":
    print("Time taken to download images using multiprocessing: {}".format(timeit.Timer(main).timeit(number=1)))