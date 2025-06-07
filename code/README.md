## Introduction to API Development

### Virtual Environment Setup

#### MacOS, Linux and GitHub CodeSpaces

```console
$ python3 -m venv env 
$ source env/bin/activate
$ pip install -r requirements.txt
```

#### Windows

```console
> pip install virtualenv 
> virtualenv env
> pip install -r requirements.txt
```

### Railway Setup

1. Go to [Railway](https://railway.app/) and Sign-Up/login for free.
2. [Railway Dashboard](https://railway.app/dashboard) -> `New Project` -> `Deploy from GitHub Repo`
3. Follow the on-screen instructions to connect your GitHub account to Railway. 
3. Select the GitHub `Repository Name` (e.g., `SMU.hack-API-Development`) ->  `Deploy now`
4. Go to `Project Settings` -> `Generate Domain`
5. Go to the `deployment url` to preview the API. 

### Run Live Server
> Run the Uvicorn live server to serve the API

```console
$ uvicorn main:app --reload
```

### To run tests in the deploy folder
```
pytest ./deploy/tests/test_main.py
```

### To run the index.html on port 5000 in the deploy folder
```
python -m http.server 5000
```
### Special Instructions for GitHub CodeSpaces

If you are running on GitHub CodeSpaces, you will need to change the API_URL variable in the index.html to the URL assigned to your CodeSpace. 

For example, instead of `const API_URL = 'http://127.0.0.1:8000';`, change to `const API_URL = 'https://opulent-space-acorn-4q4pjwgv9wv27wx-8000.app.github.dev';`

Refer to this [guide](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace) for more details

