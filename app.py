from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined list of ITGC controls
controls = [
    "User Access Management",
    "Change Management",
    "Backup and Recovery",
    "Incident Management",
    "Patch Management"
]

@app.route('/')
def index():
    return render_template('index.html', controls=controls)

@app.route('/report', methods=['POST'])
def report():
    results = []
    for control in controls:
        status = request.form.get(f"status_{control}")
        comment = request.form.get(f"comment_{control}")
        results.append({
            'control': control,
            'status': status,
            'comment': comment
        })
    return render_template('report.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
