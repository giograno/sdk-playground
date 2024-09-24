VENV_CMD ?= python3 -m venv
VENV_DIR ?= .venv
VENV_RUN = . $(VENV_DIR)/bin/activate
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
	rm -rf localstack-sdk/localstack/generated/api			# cleanup generated apis
	rm -rf localstack-sdk/localstack/generated/models		# cleanup generated models

.PHONY: venv clean
