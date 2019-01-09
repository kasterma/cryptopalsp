.PHONY: test
test:
	tox

.PHONY: venv
venv:
	python3.7 -m venv venv
	source venv/bin/activate; pip install -r requirements.txt
