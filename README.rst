Vdate
=====

Vdate is a validation library for Python.


Writing translations
--------------------

If you have added new messages int the code, don't forget to extract messages to template::

    ./setup.py extract_messages

If you're creating a new translations set, for example for "fr" language, you should initialize a new messages catalog::

    ./setup.py init_catalog --locale=fr

Or, if you need to update an existing catalog for the same language::

    ./setup.py update_catalog --locale=fr

