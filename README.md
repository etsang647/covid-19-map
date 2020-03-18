# covid-19-map

An interactive map of COVID-19 cases in the United States (will be hosted soon!).

## To build the project locally:

### Dependencies

- Python 3
- Vue CLI 4

Open a terminal in the project's root directory and execute the following:

```bash
# build client
cd client
npm i

# build server
cd ../server
python3 venv env
source env/bin/activate
pip install -r requirements.txt # potentially buggy
```

If `pip` throws an error, then install Flask and Flask-CORS manually:

```bash
pip install Flask Flask-Cors
```

All done!

## To run the project locally:

### Client

```bash
# from root
cd client
npm run serve
```

### Server

```bash
# from root
cd server
source env/bin/activate # if not already in virtual environment
python3 app.py
```
