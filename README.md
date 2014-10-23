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
