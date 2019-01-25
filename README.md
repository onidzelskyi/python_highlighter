Highlighter
===

Sample Python application that demonstrate the possibility to find and mark text sequence in web page

## How to run
To run highlighter app:
```buildoutcfg
python main.py
```

then go to [localhost:5000](localhost:5000)

## Tests
The application contains tests. To run tests:
```buildoutcfg
pytest tests
```

## Code style check
Code **must** satisfy [PEP008](https://www.python.org/dev/peps/pep-0008/) code style requirements

```buildoutcfg
pylint .
```
## TODO

 - Create **dev** branch. You can do it either via Pycharm' menu (see the Pycharm how to for details) or via terminal like this:
 ```buildoutcfg
 git checkout master
 git pull
 git checkout -b dev
```
 - Add an implementation to methods in the **main.py** module that covers the demands
    - markup_text
    - highlight_text
 - Add tests to the implemented methods in the **tests/highlighter_test.py** module
 - Run tests
 - Run code check
 - Commit and push your local changes to the remote **git** repository. You can do it either via Pycharm view (**Ctrl + K**) or via terminal 
 ```buildoutcfg
git commit -a -m 'type your commit message here'
git push origin dev
```
 - Create **MR** (merge request). See how to do it [here](https://docs.gitlab.com/ee/gitlab-basics/add-merge-request.html)
 - Send the link to the **MR** to your reviewer
 
