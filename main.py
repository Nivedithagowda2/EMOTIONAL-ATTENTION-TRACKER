from flask import Flask, render_template, Response, jsonify
from tracker import generate_frames, get_attention_stats

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')   # load HTML page

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stats')
def stats():
    data = get_attention_stats()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    



