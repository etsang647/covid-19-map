# COVID-19 Map

An interactive map of COVID-19 cases in the United States. Visit it [here](https://covid-map-usa.herokuapp.com/)!

## FAQ

### Many states show as having 0 cases for the day. Is this accurate?

No, [more than half of states do not report new data every day](https://www.washingtonpost.com/graphics/2020/national/coronavirus-us-cases-deaths/?state=US), so cases often get bunched up and reported only on certain days of the week. This is especially true on weekends, when most states will wait until Monday to report all their data.

### I'm seeing negative cases/deaths for a state. Why is that?

Some states will report negative cases/deaths for a day if prior data is found to be inaccurate and needs adjustment, and the adjustment exceeds the number of new cases/deaths for that day.

This typically happens when a number of probable cases/deaths previously reported by a state gets disproven at a later date. This state will then report negative cases/deaths for a day to adjust for that change and keep their overall case numbers accurate.

Another reason why this may happen (specifically for deaths) is that sometimes a state will change how they classify deaths attributed to COVID-19 by making their criteria stricter. After such a change the state will likely report [a large number of negative deaths for the day](https://www.boston.com/news/coronavirus/2022/03/10/covid-19-deaths-massachusetts-adjusted-count/) to keep their overall death numbers in line with the new criteria.

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
# install client dependencies
cd client
npm install

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

**Update - 03/29/2020:** Data is now automatically pulled from [The New York Times](https://github.com/nytimes/covid-19-data) upon reload. I am no longer using the [JHU CSSE dataset](https://github.com/CSSEGISandData/COVID-19) due to their recent formatting inconsistencies. Any files utilizing that dataset can be found [here](https://github.com/etsang647/covid-19-map/tree/master/server/archive/jhu_csse).

If you require data from the [JHU CSSE](https://github.com/CSSEGISandData/COVID-19) for any reason, the following instructions will still work, albeit only for the date range `01-22-2020` to `03-21-2020` prior to their data overhaul. From the `server/archive/jhu_csse` directory, run:

```bash
# for initial dependencies
npm install

# to pull US state-level data from their repository
./update_data.sh
```

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

Note: When running the server locally, make sure the `path` listed in `Home.vue`
is that of the local server (http://localhost:5000/data) and not the
production server.
