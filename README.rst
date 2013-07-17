===========================
       nose-timelimit
===========================

`nose-timelimit` is a nose plugin that allows you automatically skip slow tests.

It requires at least one run with the whole suite to register the timings. If a test fails timings 
are not registered for it (thus it will never get skipped).

Installation
============

Just run ``pip install nose-timelimit`` or ``easy_install nose-timelimit``.

Options
=======

* ``--with-timelimit`` - Just activates the plugin (will only register timing data).
* ``--timelimit=X`` - Runs only the tests that had previously ran under ``X`` seconds. Implies ``--with-timelimit``.
* ``--timelimit-silent`` - Don't print the duration for each test.

Requirements
============

Known to work with ``nose 1.3``, it may work with nose as old as ``0.10`` - try it.

