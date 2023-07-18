install:
	python3 -m venv env

run:
	env/bin/python3 src/app/models/client.py
	
test:
	pytest src/tests/client-test.py