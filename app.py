from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': '1',
  'title': 'Data analyst',
  'location': 'Agadir,Morocco',
  'salary': '8000 MAD'
}, {
  'id': '2',
  'title': 'Data scientist',
  'location': 'Casablanca,Morocco',
  'salary': '9000 MAD'
}, {
  'id': '3',
  'title': 'Back-end engineer',
  'location': 'Agadir,Morocco',
  'salary': '12500 MAD'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name='Soufiane')


@app.route("/api/jobs")  #url doesn't return html
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
