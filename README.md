# COVID-19 Map

An interactive map of COVID-19 cases in the United States (will be hosted soon!).

## To build the project locally:

### Dependencies

- [Vue CLI 4](https://cli.vuejs.org/)
- [Python 3](https://www.python.org/)
  - [pip and venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) if not already included with Python

Open a terminal window in the project's root directory and execute the following:

```bash
# install client dependencies
cd client
npm i

# install server dependencies
cd ../server
python3 venv env
source env/bin/activate
pip3 install -r requirements.txt # potentially buggy
```

If `pip3` throws an error in the last step, install Flask and Flask-CORS manually:

```bash
pip3 install Flask Flask-Cors
```

You're all set now!

## To run the project locally:

### Client

From the project root directory,

```bash
cd client
npm run serve
```

then head over to http://localhost:8080/ to visit the app.

### Server

From the project root directory,

```bash
cd server
source env/bin/activate # if not in virtual environment
python3 app.py
```

then head over to http://localhost:5000/ to visit the server.
