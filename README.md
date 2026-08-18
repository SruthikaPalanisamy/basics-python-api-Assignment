### LMS FRAPPE ASSUGNMENTa

Assignment 1: basics-API Assignment

Files

- Hooks.py -  ‎library_management/hooks.py
- API.py   -  ‎library_management/library_management/api.py

  Drive Link:
  https://drive.google.com/drive/folders/1YIYD9ueNxCXWisuyBUmmg_8RXuiDwb99?usp=sharing


Assignment 2: Python API documentation Assignment
-assignment.py  -  ‎library_management/library_management/api2.py

Drive Link:


### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch main
bench install-app library_management
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/library_management
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade
### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
