VENV_CMD ?= python3 -m venv
VENV_DIR ?= .venv
VENV_RUN = . $(VENV_DIR)/bin/activate
TEST_PATH ?= .
TEST_EXEC ?= python -m
PYTEST_LOGLEVEL ?= warning
PIP_CMD ?= pip

$(VENV_ACTIVATE): pyproject.toml
	test -d $(VENV_DIR) || $(VENV_BIN) $(VENV_DIR)
	$(VENV_RUN); $(PIP_CMD) install --upgrade pip
	touch $(VENV_ACTIVATE)

venv: $(VENV_ACTIVATE)    ## Create a new (empty) virtual environment


build-spec:			## build the entire localstack api spec (openapi.yaml in the root folder)
	$(VENV_RUN); python scripts/create_spec.py

clean: clean-generated         	## Clean up
	rm -rf $(VENV_DIR)

clean-generated:	## Cleanup generated code
	rm -rf localstack-sdk/localstack/generated/api/*.py
	rm -rf localstack-sdk/localstack/generated/models/*.py
	touch localstack-sdk/localstack/generated/api/__init__.py
	touch localstack-sdk/localstack/generated/models/__init__.py

test:              		  ## Run automated tests
	($(VENV_RUN); $(TEST_EXEC) pytest --durations=10 --log-cli-level=$(PYTEST_LOGLEVEL) $(PYTEST_ARGS) $(TEST_PATH))

.PHONY: venv clean
