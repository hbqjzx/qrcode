from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()       
    url = "https://api.zhishuyun.com/qrart/generate?token=" + data['token']    
    headers = { "accept": "application/json", "content-type": "application/json" }
    data['steps'] = 16 if 10 > int(data['steps']) or int(data['steps']) > 20 else int(data['steps'])
    data['qrw'] = 1.5 if 0.1 > float(data['qrw']) or float(data['qrw']) > 3 else float(data['qrw'])
    data['seed'] = 998899 if 1 > int(data['seed']) or int(data['seed']) > 9007199254740991 else int(data['seed'])

    payload = {
      "prompt": data['prompt'],
      "content": data['content'],
      "type": data['type'],
      "pattern": data['pattern'],      
      "preset": data['preset'],
      "steps": data['steps'],
      "qrw": data['qrw'],
      "seed": data['seed'],
      "rawurl": data['rawurl']
    }    

    response = requests.post(url, json=payload, headers=headers)    
#     response={
#   "task_id": "db821724-2fc1-4e16-a506-d30742539e13",
#   "image_url": "https://qrart.cdn.zhishuyun.com/attachments/1132182283529494652/1136073065839730818/Germey_2023-08-01__64c99070434f8771e9c97b29.png",
#   "image_width": 768,
#   "image_height": 768
# }    
    #if response!='':#.status_code == 200:
    if response.status_code == 200:
        #json_data = response#.json()        
        json_data = response.json()        
        result = {
            "success": True,
            "task_id": json_data['task_id'],
            "image_url": json_data['image_url'],
            "image_width": json_data['image_width'],
            "image_height": json_data['image_height']
        }        
        return jsonify(result)        
    else: 
        return jsonify({'success': False})
if __name__ == '__main__':
    app.run(debug=True)
