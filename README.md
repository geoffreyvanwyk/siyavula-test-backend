# Wikipedia TOC Fetcher
This application displays the table of contents of the Wikipedia page specified by the user. The user enters the URL of any Wikipedia page into a text box, then clicks a submit button. A new page is then loaded, containing only the table of contents of the entered page.

## Installation
These instructions are for Ubuntu 14.04.

### Python
Install Python:

    $ sudo aptitude install python

Set path to Python virtual environment:

    $ echo 'export $VENV=$HOME/.pyvenv' >> $HOME/.bashrc

Create Python virtual environment:

    $ pyvenv-3.4 --without-pip $VENV
    $ source $VENV/bin/activate
    $ curl https://bootstrap.pypa.io/get-pip.py | python
    $ deactivate
    $ source $VENV/bin/activate

Install setuptools:

    $ wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | $VENV/bin/python

### Pyramid
Install Pyramid web framework:

    $ easy_install pyramid

Install dependencies:

    $ easy_install pyramid_jinja2 

Install development dependencies:

    $ easy_install pyramid_debugtoolbar nose webtest  

## Usage
Setup the project:

    $ python setup develop

Run the tests:

    $ nosetests table_of_contents

Start the web server:

    $ pserve developement.ini --reload 

View the application in a web browser at http://localhost:6543.

## Licence
Copyright © 2015 Geoffrey B. van Wyk <geoffrey@vanwyk.biz>

This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
