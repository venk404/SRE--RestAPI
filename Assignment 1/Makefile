.ONESHELL:
VENV := venv

all: install Schema-creation run

# Define the installation steps
install: $(VENV)\Scripts\activate

$(VENV)\Scripts\activate: requirements.txt
	python -m venv $(VENV)

ifeq ($(OS),Windows_NT)
	$(VENV)\Scripts\activate.ps1
	$(VENV)\Scripts\python -m pip install --upgrade pip
	$(VENV)\Scripts\pip install -r requirements.txt
else
	chmod +x $(VENV)/bin/activate
	source $(VENV)/bin/activate
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt
endif

Schema-creation:
ifeq ($(OS),Windows_NT)
	$(VENV)\Scripts\python DB\Schemas\Create_Student.py
else
	$(VENV)/bin/python DB/Schemas/Create_Student.py
endif

# Define the run step
run:
ifeq ($(OS),Windows_NT)
	uvicorn Main:app --reload
else
	uvicorn Main:app --reload
endif

# Define a clean step
clean:
ifeq ($(OS),Windows_NT)
	@if exist $(VENV) rmdir /s /q $(VENV)
	@powershell -Command "Get-ChildItem -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force"
else
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} \;
endif

test:
ifeq ($(OS),Windows_NT)
	$(VENV)\Scripts\python test.py
else:
	$(VENV)\bin\python test.py
endif


.PHONY: install run clean reinstall

