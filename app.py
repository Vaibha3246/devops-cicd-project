from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello DevOps Engineer Vaibhav!"


@app.route('/version')
def version():
    return {
        "application": "devops-cicd-project",
        "version": "v2"
    }

@app.route('/health')
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)