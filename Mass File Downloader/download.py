import requests

def DownloadFile(url, index):
    local_filename = f"audio_files/Unit {index}.mp3"
    r = requests.get(url)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    return None

file_name = input("Enter url filename (ex urls.txt): ")
url_list = open(file_name, "r").read().splitlines()

index = 1
for url in url_list:
    url = requests.head(url, allow_redirects=True)
    print(f"Downloading File {index} from {url.url}")
    DownloadFile(url.url, index)
    index+=1
print("Done!")