# COVID-19 Map

An interactive map of COVID-19 cases in the United States (will be hosted soon!).

## To build the project locally

### Install dependencies

- [Vue CLI 4](https://cli.vuejs.org/)
  - [Node.js](https://nodejs.org/)
    - [npm](https://www.npmjs.com/) (included with Node)
- [Python 3](https://www.python.org/)
  - [pip and venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) (included with Python 3)

Then open a terminal window in a directory of your choice and execute the following:

```bash
# clone repository (copy URL from address bar)
git clone https://github.com/etsang647/covid-19-map

# enter project directory
cd covid-19-map

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

## To run the project locally

### Client

From the project root directory, execute:

```bash
cd client
npm run serve
```

The app should then be hosted at http://localhost:8080/.

### Server

From the project root directory, execute:

```bash
cd server
source env/bin/activate # if not in virtual environment
flask run
```

The server should then be hosted at http://localhost:5000/.
