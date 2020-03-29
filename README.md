# COVID-19 Map

An interactive map of COVID-19 cases in the United States (will be hosted soon!).

## To build the project locally

### Install dependencies

- [Vue CLI 4](https://cli.vuejs.org/)
  - [Node.js](https://nodejs.org/)
    - [npm](https://www.npmjs.com/) (if not already included with Node)
- [Python 3](https://www.python.org/)
  - [pip and venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) (if not already included with Python)

Open a terminal window in a directory of your choice and clone the repository using the project URL from your address bar:

```bash
git clone https://github.com/etsang647/covid-19-map
```

Enter the project directory and install the rest of the dependencies:

```bash
# install project dependencies
cd covid-19-map
npm i

# install client dependencies
cd client
npm i

# install server dependencies
cd ../server
python3 venv env
source env/bin/activate
pip3 install -r requirements.txt # potentially buggy
```

If `pip3` throws an error in the last step, install [Flask](https://pypi.org/project/Flask/) and [Flask-CORS](https://pypi.org/project/Flask-Cors/) manually:

```bash
pip3 install Flask Flask-Cors
```

You're all set!

### (optional) Refresh data

~~From the `server` directory, run `make data` to pull the most recent COVID-19 data from [JHU CSSE](https://github.com/CSSEGISandData/COVID-19).~~

**Update as of 03/29/2020:** Data is now automatically pulled from [The New York Times](https://github.com/nytimes/covid-19-data) upon reload. I am no longer using the [JHU CSSE dataset](https://github.com/CSSEGISandData/COVID-19) due to their recent formatting inconsistencies.

## To run the project locally

### Client

From the `client` directory, run

```bash
npm run serve
```

to host the app at http://localhost:8080/.

### Server

From the `server` directory, run

```bash
source env/bin/activate # if not in virtual environment
flask run
```

to host the server at http://localhost:5000/.
