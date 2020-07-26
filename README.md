## parse-path script

#### Script for Windows dev environments to produce a posix-compliant tree of the ```node_modules``` directory with slashes the right direction to simply copy-paste ```node_module``` locations for your projects
 (probably most useful for front-end web developers, but may have other applications)

Assumption:  mingw64-git bash terminal for Windows, python 3, and nodejs with commands in $PATH installed for basic dev environment.

First, install tree-cli globally:

```bash
$ npm i -g tree-cli
```

Then, clone this repo: 

```bash
$ git clone git@github.com:averyfreeman/parse-path.git
```

Then, copy all files to your npm project's documentRoot and run script:

```bash
$ cp * ~/nodejs/rad_project_1/
$ cd ~/nodejs/rad_project_1
$ npm init
$ npm i module1 module2
$ ./parse-path.sh
```

It should generate a tree-view with full path names for your ```node_modules``` directory called ```tree.txt``` and display it using ```less``` 

You can edit the ```.sh``` script to have it open in ```notepad.exe```, ```subl.exe```, or ```code.exe```, etc. - something more Windows-friendly... or just open another bash terminal and keep the ```less``` display and copy from there.

For reference, here are the two scripts:

```bash
tree -l 8 node_modules --fullpath --noreport -o tree.txt
python parse-path.py
less tree.txt
```

The ```tree``` command goes eight directories deep in its recursion - if you need it to go further, just edit the script.  ```--noreport``` prevents it from printing out the unnecessary non-parsed Windows backward-slash version ```tree``` creates before the python script parses it, which is useless for anything besides Windows machines.

```python
import fileinput

filename = "./tree.txt"
open(filename).read()
print("\n\tReplaced \\ with / and saved as "+ filename)
with fileinput.FileInput(filename, inplace=True) as file:
    for str in file:
        print(str.replace('\\', '/'), end='')
print("all done")
```
