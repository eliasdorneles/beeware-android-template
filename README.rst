BeeWare Android Template
========================

A template for starting a native Android app using Python and the BeeWare tools.

More specifically, it uses `VOC`_ for compiling Python into Java bytecode
and `Briefcase`_ to package as an Android app.

Using this template
-------------------

**Requirements:** you need to have Python 3, Java JDK and the `Android SDK`_ installed

0. Create a virtualenv using Python 3 (3.5 recommended).

1. Install `cookiecutter`_. This is a tool used to bootstrap complex project
   templates::

    $ pip install cookiecutter

2. Run ``cookiecutter`` on this template::

    $ cookiecutter https://github.com/eliasdorneles/beeware-android-template

3. Add your code to the project.

4. Install `Briefcase`_. This is a tool that produces a version of your
   project that can be deployed to specific platforms::

    $ pip install briefcase

5. Start the Android emulator or `connect your Android device`_

6.  Build and run your app with::

    $ python setup.py android --start



Example apps
------------

* `TicTacToe`_ (created before this template, but using the same building blocks)
* `Drawing app`_ (created with this template)
* `Todo app`_ (created with this template)

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _briefcase: https://github.com/pybee/briefcase
.. _VOC: https://github.com/pybee/voc
.. _TicTacToe: https://github.com/eliasdorneles/tictactoe-voc
.. _Drawing app: https://github.com/eliasdorneles/drawingapp-voc
.. _Todo app: https://github.com/eliasdorneles/todoapp-voc
.. _Android SDK: https://developer.android.com/studio/index.html#downloads
.. _APK: https://en.wikipedia.org/wiki/Android_application_package
.. _connect your Android device: https://code.tutsplus.com/articles/connecting-physical-android-devices-to-your-development-machine--mobile-12376
