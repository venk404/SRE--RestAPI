.ONESHELL:
VENV := venv

all: install run

# Define the installation steps
install: $(VENV)/Scripts/activate

$(VENV)/Scripts/activate: requirements.txt
	python -m venv $(VENV)
ifeq ($(OS),Windows_NT)
	$(VENV)\Scripts\activate.ps1
	$(VENV)\Scripts\python -m pip install --upgrade pip
	$(VENV)\Scripts\pip install -r requirements.txt
else
	chmod +x $(VENV)/bin/activate
	. $(VENV)/bin/activate
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt
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
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
else
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} \;
endif

# Define a target for reinstallation
reinstall: clean install

.PHONY: install run clean reinstall

