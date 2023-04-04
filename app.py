import os

from flask import Flask, request, render_template, Response
from tqdm import tqdm
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def download_file():
    if request.method == 'POST':
        session = requests.Session()
        login_data = {
            'username': "stvz02",
            'password': "stvz02**"
        }
        session.post("https://anuarioeco.uo.edu.cu/index.php/aeco/login/signIn", data=login_data)
        input_str = request.form['files']
        try:
            files_dict = json.loads(input_str)
            if isinstance(files_dict, dict):
                files_dict = [files_dict]
        except:
            id_archive, filename = input_str.split()
            files_dict = [{"id": id_archive, "name": filename}]
        for file_dict in files_dict:
            id_archive = file_dict["id"]
            filename = file_dict["name"]
            download_url = f'https://anuarioeco.uo.edu.cu/index.php/aeco/$$$call$$$/api/file/file-api/download-file?submissionFileId={id_archive}&submissionId=5736&stageId=1'
            response = session.head(download_url)
            response = session.get(download_url, stream=True)
            total_size_in_bytes = int(response.headers.get('content-length', 0))
            block_size = 1024
            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
            def generate():
          #      with open('/storage/emulated/0/Download/'+filename, 'wb') as file:
          #          for data in response.iter_content(block_size):
          #              progress_bar.update(len(data))
           #             file.write(data)
          #              yield data
            #    progress_bar.close()
            headers = {
                'Content-Disposition': f'attachment; filename="{filename}"',
                'Content-Type': 'application/octet-stream',
                'Cache-Control': 'no-cache'
            }
            return Response(generate(), headers=headers)
    else:
        return render_template('index.html')
