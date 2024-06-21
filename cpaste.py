import requests

def upload_file(file_path):
    url = 'https://paste.c-net.org/'

    # Open the file and read its content as binary
    with open(file_path, 'rb') as f:
        files = {'file': (file_path, f)}

        # Make the multipart/form-data request
        try:
            response = requests.post(url, files=files)
            response.raise_for_status()
            print('Upload successful!')
            print(response.text)  # Optionally print the response from the server
        except requests.exceptions.RequestException as e:
            print(f'Error uploading file: {e}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python upload_file.py <file_path>')
        sys.exit(1)

    file_path = sys.argv[1]
    upload_file(file_path)
