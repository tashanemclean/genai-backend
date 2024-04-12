# genai-backend

## Section 1: Local Development Environment Setup

### Setup Virtual Environment

To use this miroservice, you need to have the following tools installed on your
developer machine:

1. Python 3 preferred [Python](https://www.python.org/)
2. pip [Pip](https://pypi.org/project/pip/)
3. venv, [venv](https://docs.python.org/3/library/venv.html)

```
$ python3 -m venv venv
$ source venv/bin/activate
```

### Install OpenAI

The OpenAI API requires authentication through a secret key that you can
retrieve [here](https://platform.openai.com/api-keys) once logged in to your
account.

```
$ pip install openai
```

### Install Dependencies

```
$ pip install openai
$ pip install Flask
$ pip install python-dotenv
```

### Configure Environment variables

To use environment variables, create .env in project root directory and update
values

```
PORT=9000
HOST=localhost
OPEN_API_KEY=<openai-api-key>
```

### Running the app

When running with flask, `flask run` will not read in environment variables and
app will start on the default port 5000.

To run , run:

```
$ python app.py
```

## Limitations

Take care when exceeding your plan quota, the api will fail and you may need to
adjust your billing details, read the docs:
https://platform.openai.com/docs/guides/error-codes/api-errors.