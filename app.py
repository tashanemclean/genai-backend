from flask import Flask, request, Response
from flask_cors import CORS

from internal import logger
from internal.classify import text

log = logger.logger

app = Flask(__name__)
methods = ["OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]
CORS(app, origins=["*"], methods=methods, send_wildcard=True)

def main():
    app.run()

@app.route('/_health')
def health():
    return Response({"App": "GenAI Backend", "Version": "0.1", "Message": "OK"}, mimetype="application/json", status=200)

@app.route('/api/text', methods=['POST'])
def prompt_completions():
    form_data = request.get_json()
    prompt = form_data["text"]
    result = text.Prompt(prompt)
    content = result.get()
    log.info("classify_text request")
    return Response(content[0].message.content, mimetype="application/json", status=200)

    
if __name__ == "__main__":
    main()