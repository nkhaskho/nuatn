
Author: Naiim Khaskhoussi
## Python interview
<br>

#### Create virtual environment
Create a virtual environment using the command below, and by replacing the **<env_name>** by the desired name for your environment.
``` bash
python3 -m venv <env_name>
```
<br>

#### Activate the virtual environment
``` bash
source <env_name>/bin/activate
```
<br>

#### Install required packages

``` bash
pip install -r requirements.txt
```
The requirements.txt file was generated using the **pip freeze > ...** command. This file contain a list of all external package used for this project (django, django-rest-framework,...)

<br>

#### Run the server
``` bash
python3 manage.py runserver
```
<br>
