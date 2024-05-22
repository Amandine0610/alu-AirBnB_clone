<h1 align="center">alu-AirBnB</h1>
<p align="center">
  <img src="https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png" alt="AirBnB Logo" width="200">
</p>
<p align="center">An AirBnB clone.</p>

---

## Description :house:

HBnB is a comprehensive web application that integrates database storage, a backend API, and frontend interfacing, creating a clone of AirBnB. This initial phase focuses on developing a custom command-line interface for data management and establishing the base classes for data storage.

## Usage :computer:

The console operates in both interactive and non-interactive modes, similar to a Unix shell. It displays a prompt **(hbnb)**, awaiting user input.

### Command Examples

| Command                                       | Example                                                                                                                                    |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Run the console                               | `./console.py`                                                                                                                             |
| Quit the console                              | `(hbnb) quit`                                                                                                                              |
| Display help for a command                    | `(hbnb) help <command>`                                                                                                                    |
| Create an object (prints its id)              | `(hbnb) create <class>`                                                                                                                    |
| Show an object                                | `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)`                                                                                  |
| Destroy an object                             | `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)`                                                                            |
| Show all objects, or all instances of a class | `(hbnb) all` or `(hbnb) all <class>`                                                                                                       |
| Update an attribute of an object              | `(hbnb) update <class> <id> <attribute name> "<attribute value>"` or `(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")` |

### Non-interactive Mode Example

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

