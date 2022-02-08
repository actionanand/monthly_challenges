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
- [Built-in template tags and filters](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/)

### Extensions

- [Django by Baptiste Darthenay](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
- [Python by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Pylance by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Best Visual Studio Code Extensions for Python/Django](https://blog.devgenius.io/best-visual-studio-code-extensions-for-python-django-af2fdbf7198a)

### More on the Django Template Language (DTL)

1.  Accessing Dictionary Fields in Templates

When accessing dictionary data in a template, you DON'T use this syntax:

```python
{{ myDictionary['some_key'] }}
```

Instead, you use the dot notation - as if it were a regular Python object:

```python
{{ myDictionary.some_key }}
```

This might look strange, but keep in mind, that the DTL is a custom-made language. It looks like Python, but ultimately it is NOT Python - it's a language parsed and executed by Django. Hence, its syntax can deviate - just as it does here.

2. Calling Functions in Templates

Calling functions in templates also works differently than it does in Python.

Instead of calling it, you use functions like regular variables or properties.

I.e., instead of:

```python
{{ result_from_a_function() }}
```

you would use

```python
{{ result_from_a_function }}
```