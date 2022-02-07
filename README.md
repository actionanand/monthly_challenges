# Monthly Challenges

> it's a Django project

### How to create a project?

```bash
django-admin startprojrct <project-name>
```

## After creating proj., how to create a app?

```
cd <project-name>
python3 manage.py startapp <app-name>
```

```
python3 manage.py startapp challenges
```

### How to run a dev server?

```bash
cd <project-name>
python3 manage.py runserver
```

### How to install Django?

```bash
python3 -m pip install Django
```

after this try to run the below command

```bash
django-admin
```

if the above command doesn't run, please run the below command

```bash
pip3 uninstall django
sudo pip3 install django
```

### How to install python in WSL?

```bash
sudo apt update && upgrade
sudo apt install python3 python3-pip ipython3
```

### How to undo all uncommitted and unsaved git changes?

```bash
git stash -u && git stash drop
```


### Resources

- [Python setup on the Windows subsystem for Linux (WSL)](https://medium.com/@rhdzmota/python-development-on-the-windows-subsystem-for-linux-wsl-17a0fa1839d)
- [Stackoverflow - git undo all uncommitted or unsaved changes](https://stackoverflow.com/a/56511464/10907720)
- [Path converters](https://docs.djangoproject.com/en/3.2/topics/http/urls/#path-converters)