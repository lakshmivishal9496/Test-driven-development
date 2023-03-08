PYTHON :=
ifeq ($(OS),Windows_NT)
	PYTHON=.venv\Scripts\python
else
	PYTHON=.venv/bin/python
endif

venv:
	test -d .venv || python -m venv .venv/

install-requirements: check-venv
	$(PYTHON) -m pip install --upgrade -q pip
	$(PYTHON) -m pip install -r requirements.txt

install-toml: check-venv
	$(PYTHON) -m pip install --upgrade -q pip
	$(PYTHON) -m pip install .

## creates dist files and package release files based on pyproject.toml (depends on check-virtual-env)
build-toml: install-toml
	$(PYTHON) -m pip install --upgrade -q pip
	$(PYTHON) -m build

# ---------------------------------------------------------
# Cleanup generated and installed files.

clean: 
	find . -name '*.coverage *.pyc' -exec rm -f {} + 
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf .coverage htmlcov 


clean-all: clean-build clean-pyc clean-test clean-doc clean-src clean-venv

clean-docs:
	rm -rf docs/build

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-src:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


run: check-venv
	@$(PYTHON) src/main.py

check-venv:
	@if [ -z "$$(which python | grep -o .venv)" ]; then \
		exit 1; \
	fi

pylint: check-venv
	@find src/ -name '*.py' -print0 | xargs -0 pylint -d C0103 -rn

test: check-venv
	$(PYTHON) -m unittest discover -p 'test_*.py' -v -b

flake8: check-venv
	@$(call MESSAGE,$@)
	-flake8 --exclude=.svn,CVS,.bzr,.hg,.git,__pycache__,.tox,.nox,.eggs,*.egg,.venv,venv,*.pyc

black: check-venv
	@$(call MESSAGE,$@)
	-black --check --diff src/

coverage: check-venv
	@$(call MESSAGE,$@)
	-coverage run -m unittest discover -p 'test_*.py' -v -b
	-coverage html
	-coverage report -m

cohesion: check-venv
	@$(call MESSAGE,$@)
	-$(PYTHON) -m radon cc src/ -a -nc

.PHONY: pydoc 
pydoc: check-venv
	@$(call MESSAGE,$@)
	-$(PYTHON) -m pydoc -w src/*.py

pdoc: check-venv
	@$(call MESSAGE,$@)
	-$(PYTHON) -m pdoc --html --output-dir docs/ src/*.py
	

doc: check-venv
	@$(call MESSAGE,$@)
	-$(PYTHON) -m pdoc --html --output-dir docs/ src/*.py 

lint: flake8 check-venv
	@$(call MESSAGE,$@)
