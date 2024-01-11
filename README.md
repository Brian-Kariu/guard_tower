<a name="readme-top"></a>

<br />
<div align="center">
  <a">
    <img src="assets/img/padlock.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Authserver</h3>

  <p align="center">
    Never write authentication for your projects again!
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#docker-install">Docker Install</a></li>
        <li><a href="#running-locally">Running Locally</a></li>
        <li><a href="#dev-containers">Dev Containers</a></li>
      </ul>
    </li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#shell">Shell</a></li>
    <li><a href="#running-tests/linter">Running Tests/linter</a></li>
    <li><a href="#migrations">Migrations</a></li>
    <li><a href="#asset-management">Asset Management</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About The Project

I got tired writing authentication workflows for my apps and third party solutions didn't work out for me. So i made an authserver for all my apps. Super safe😅.

## Getting started

### Docker Install

This app can be run completely using `Docker` and `docker-compose`. **Using Docker is recommended, as it guarantees the application is run using compatible versions of Python and Node**.

There are three main services:

To run the development version of the app

```bash
docker-compose up flask-dev
```

To run the production version of the app

```bash
docker-compose up flask-prod
```

The list of `environment:` variables in the `docker-compose.yml` file takes precedence over any variables specified in `.env`.

To run any commands using the `Flask CLI`

```bash
docker-compose run --rm manage <<COMMAND>>
```

Therefore, to initialize a database you would run

```bash
docker-compose run --rm manage db init
docker-compose run --rm manage db migrate
docker-compose run --rm manage db upgrade
```

A docker volume `node-modules` is created to store NPM packages and is reused across the dev and prod versions of the application. For the purposes of DB testing with `sqlite`, the file `dev.db` is mounted to all containers. This volume mount should be removed from `docker-compose.yml` if a production DB server is used.

Go to `http://localhost:8080`. You will see a pretty welcome screen.

### Running locally

Run the following commands to bootstrap your environment if you are unable to run the application using Docker

```bash
cd shell_scripts
./manual_deploy.sh
```

### Dev Containers

The best option to get started if you are using vscode however is to use dev containers. Simple open the command pallete and search for `Dev Containers: Open Folder in containers...`. It will start the dev environment with everything set up.

Go to `http://localhost:5000`. You will see a pretty welcome screen.

#### Database Initialization (locally)

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration

```bash
flask db init
flask db migrate
flask db upgrade
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Deployment

When using Docker, reasonable production defaults are set in `docker-compose.yml`

```text
FLASK_ENV=production
FLASK_DEBUG=0
```

Therefore, starting the app in "production" mode is as simple as

```bash
docker-compose up flask-prod
```

If running without Docker

```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
export DATABASE_URL="<YOUR DATABASE URL>"
npm run build   # build assets with webpack
flask run       # start the flask server
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Shell

To open the interactive shell, run

```bash
docker-compose run --rm manage shell
flask shell # If running locally without Docker
```

By default, you will have access to the flask `app`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Running Tests/Linter

To run all tests, run

```bash
docker-compose run --rm manage test
flask test # If running locally without Docker
```

To run the linter, run

```bash
docker-compose run --rm manage lint
flask lint # If running locally without Docker
```

The `lint` command will attempt to fix any linting/style errors in the code. If you only want to know if the code will pass CI and do not wish for the linter to make changes, add the `--check` argument.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Migrations

Whenever a database migration needs to be made. Run the following commands

```bash
docker-compose run --rm manage db migrate
flask db migrate # If running locally without Docker
```

This will generate a new migration script. Then run

```bash
docker-compose run --rm manage db upgrade
flask db upgrade # If running locally without Docker
```

To apply the migration.

For a full migration command reference, run `docker-compose run --rm manage db --help`.

If you will deploy your application remotely (e.g on Heroku) you should add the `migrations` folder to version control.
You can do this after `flask db migrate` by running the following commands

```bash
git add migrations/*
git commit -m "Add migrations"
```

Make sure folder `migrations/versions` is not empty.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Asset Management

Files placed inside the `assets` directory and its subdirectories
(excluding `js` and `css`) will be copied by webpack's
`file-loader` into the `static/build` directory. In production, the plugin
`Flask-Static-Digest` zips the webpack content and tags them with a MD5 hash.
As a result, you must use the `static_url_for` function when including static content,
as it resolves the correct file name, including the MD5 hash.
For example

```html
<link rel="shortcut icon" href="{{static_url_for('static', filename='build/favicon.ico') }}" />
```

If all of your static files are managed this way, then their filenames will change whenever their
contents do, and you can ask Flask to tell web browsers that they
should cache all your assets forever by including the following line
in `.env`:

```text
SEND_FILE_MAX_AGE_DEFAULT=31556926  # one year
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

Ideally you should be able to create a super user account, login then start creating user groups for your app. Other
features would be create,edit and delete permissions for user, social authentication and even admin dashboards.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [x] Create a working jwt auth flow
- [ ] Detailed user profile
- [ ] Create user groups models for the different apps
- [ ] Create permissions for each of the groups
- [ ] Admin dashboards
- [ ] Social Authentication

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
