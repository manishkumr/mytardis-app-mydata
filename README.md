# mytardis-app-mydata
Server-side functionality and data models for MyData


This app should be installed in "tardis/apps/mydata":
```
cd /opt/mytardis/develop/tardis/apps
git clone https://github.com/wettenhj/mytardis-app-mydata mydata
```
When cloning the repository above, ensure that you clone the "wettenhj/mytardis-app-mydata" repository as described above, NOT the "wettenhj/mydata" repository.

Run "pip install -r requirements.txt" from the "tardis/apps/mydata" directory to install the extra Python module dependency (django-ipware) required by the "mytardis-app-mydata" app.  If you are not using a virtualenv for your MyTardis Python module dependencies, then you may need use "sudo".

```
pip install -r requirements.txt
```

Add this app to tardis/settings.py:

```
INSTALLED_APPS += ('tardis.apps.mydata',)
```
Restart MyTardis.

Create Uploader data models:

```
python mytardis.py schemamigration mydata --initial
python mytardis.py migrate mydata
```
Restart MyTardis.

Create defaultexperiment schema from fixture:

```
python mytardis.py loaddata tardis/apps/mydata/fixtures/default_experiment_schema.json
```
