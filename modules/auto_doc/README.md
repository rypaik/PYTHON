## LINKS

[Auto-Docs for Python](https://towardsdatascience.com/auto-docs-for-python-b545ce372e2d)

[jamescalam/autodocs: Working on automatic documentation of my Python code.](https://github.com/jamescalam/autodocs)


## Functions
```
def extract_module (code):
"""
Function used to extract the top block quote containing key information
on the Python script. Including module name, developers, and description.

Parameters
----------
code : str
    Python code containing the module description in the first block quote.
    Should containing module name first, developers on a line following
    'Developers:', and description last, beginning on line following
    'Description:'.


Returns
-------
name : str
    Module name.
devs : str
    Name of developers.
desc : str
    Description of the module.
"""
```



```
def build_page(module, devs, desc, classes="", funcs="", submodule=""):
"""
Function for building HTML docs using extracted data.

Parameters
----------
module : str
    String containing the module name.
devs : str
    String containing the names of script developers.
desc :str
    String describing the module.
classes : dict, optional
    Dictionary containing classes and their description, code, functions, and variables. The default is "".
funcs : dict, optional
    Dictionary containing functions and their descriptions and parameters.
    The default is "".
submodule : str, optional
    String containing the submodule name, if within a submodule, eg class.
    The default is "".

Returns
-------
None.
"""

```



## Classes


```
class DocsBuilder:
"""
Class used for automatically generating HTML-based documentation from
Python code. Note that function docstrings must also follow NumPy/SciPy
docstring formatting conventions.
"""

def _init__(self, docs_dir='docs', offline=False):
    """
    ... docstring .. 
    """
    ... code ...


def extract(self, code):
    """
    ... docstring ...
    """
    ... code ...

def output(code, filename, path="docs") :


```



ASIDE
#regex
In regex, we write (?sm)class [\w\d_]+:.*(^\w).

    [\w\d_] matches text, numeric and underscore characters, adding + means it will match an unlimited number of these characters.
    (?sm) is again our global pattern modifier, the m flag tells the regex that we want ^ and $ to signify the start and end of a line respectively.
    (^.) is the start of a line ^ immediately followed by any character . .






