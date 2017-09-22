BeeWare Android Template
========================

A template for starting a native Android app using Python and the BeeWare tools.

More specifically, it uses `VOC`_ for compiling Python into Java bytecode
and `Briefcase`_ to package as an Android app.

**Requirements:** you need to have Python 3 and the `Android SDK`_ installed

Using this template
-------------------

0. Create a virtualenv using Python 3 (3.5 recommended).

1. Install `cookiecutter`_. This is a tool used to bootstrap complex project
   templates::

    $ pip install cookiecutter

2. Run ``cookiecutter`` on this template::

    $ cookiecutter https://github.com/eliasdorneles/beeware-android-template

3. Add your code to the project.

4. Install `Briefcase`_. This is the tool that will produce a version of your
   project that can be deployed to specific platforms::

    $ pip install briefcase

5. Use Briefcase to generate the Android artifacts::

    $ python setup.py android

6. Start the Android emulator or connect your Android device

7. Build and run your app using Gradle::

   $ (cd android && ./gradlew run)


Example apps
------------

* `TicTacToe`_ (created before this template, but using the same building blocks)
* `Drawing app`_ (created with this template)

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _briefcase: https://github.com/pybee/briefcase
.. _VOC: https://github.com/pybee/voc
.. _TicTacToe: https://github.com/eliasdorneles/tictactoe-voc
.. _Drawing app: https://github.com/eliasdorneles/drawingapp-voc
.. _Android SDK: https://developer.android.com/studio/index.html#downloads
