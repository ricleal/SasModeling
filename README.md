SasModeling
===========

Test for the future standalone package of models for SasFit

Build
-----
Just builds in place (no copy of the *.py)

```
python setup.py build_ext --inplace
```

Intall:

```
python setup.py install --user --record files.txt
```

Uninstall:

```
cat files.txt | xargs rm -rf
```

Documentation:
--------------
To generate the html documentation:

```
python setup.py docs
```

For the now the index is not working. The generated model docs are available in the folder:

```
SasModeling/docs/sphinx-docs/build/html/user/models/model_functions.html
```

Run Tests:
----------

```
cd test
python run_one.py sansmodels/test/utest_models.py
```

*Note:*

```
test/run_one.py
```

needs:

```
run.py
```

Notes:
------
- Removed the build_sphinx (but non the media files in the src/sans)
 - If to include, one needs to copy over the sasview docs/sphinx-docs folder and change the setup.py
