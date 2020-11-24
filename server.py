import json
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

team_number = 4
pa_number = 7

try:
    with open('data.json', 'r') as f:
        team_states = json.load(f)
except IOError:
    team_states = [[0,]*pa_number for _ in range(team_number)]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
@app.route('/laurence')
@app.route('/argali')
def index_admin():
    return render_template('index_admin.html')


@app.route('/update', methods=['POST'])
def update_team():
   data = request.get_json()
   team_states[data["team_idx"]][data["pa_idx"]] = data["pa_value"]
   with open('data.json', 'w') as f:
        json.dump(team_states, f)
   return ""


@app.route('/state', methods=['GET'])
def get_state():
    return jsonify(team_states)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 
