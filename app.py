from flask import Flask, jsonify, request

from internal import config, logger
from internal.classify import text

log = logger.logger

app = Flask(__name__)

def main():
    app.run(debug=True, host=config.config["HOST"], port=config.config["PORT"])

@app.route('/api/text', methods=['POST'])
def text_prompt():
    param = request.form.get("text")

    result = text.Prompt(param).get()
    log.info("classify_text request")

    return jsonify(result), 200

    
if __name__ == "__main__":
    main()