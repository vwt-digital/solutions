[![CodeFactor](https://www.codefactor.io/repository/github/vwt-digital/solutions/badge)](https://www.codefactor.io/repository/github/vwt-digital/solutions)

Solutions is a solution catalog application specific for the Google Cloud environment.

Based on the json solutions files in the /config/solutions directory a html structure is generated in the /html directory.

```bash
apt update
apt -y install virtualenv
virtualenv -p python3.7 /venv
source /venv/bin/activate

pip install -r requirements.txt

cd scripts

python3 ./transform2html.py
```


