# Hello Python

A sample application in python using [GNU Make](https://www.gnu.org/software/make/), it can be configured to use
[pipenv](https://pypi.org/project/pipenv/) or [venv](https://docs.python.org/3/library/venv.html). It also uses
[black](https://pypi.org/project/black/), [pytest](https://pypi.org/project/pytest/),
[pytest-cov](https://pypi.org/project/pytest-cov/), [mypy](https://pypi.org/project/mypy/),
and [isort](https://pypi.org/project/isort/), all running in a
[VSCode devcontainer](https://code.visualstudio.com/docs/devcontainers/containers).

## Getting started

### Python version and installation 
It's recommended to use [pyenv](https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv) to manage your python versions
```bash
curl https://pyenv.run | bash 
```

And configure your shell (for `zsh` only, refer to the [docs](https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv) for other shells):
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

Then you can just install a version and use it locally:
```bash
pyenv install
```

### Setting up the environment

Define if you'll use pipenv or virtualenv. Copy the `.env.example` file to the `.env` file and customize:
```bash
cp .env.example .env
```

Depending on which environment you're going to use, run:
```bash
make init-repo-pipenv
```
or
```bash
make init-repo-virtualenv 
source .venv/bin/activate
```

### Running the app

Run the application:
```bash
make run
```

Run the tests, lint, type check and coverage:
```bash
make check
```

The coverage report will be present in the [`htmlcov`](./htmlcov/) folder.
