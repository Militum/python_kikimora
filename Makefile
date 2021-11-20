# makefile用の設定
SHELL=/usr/bin/env bash

.PHONY: vendor
vendor:
	@cd src && pip install --upgrade -r <(pipenv lock -r) -t vendor

.PHONY: zip
zip:
	@$(MAKE) vendor
	@cd src && zip -q -x "*__pycache__*" -r ../src.zip *
