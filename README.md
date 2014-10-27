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

For now the index is not working. The generated model docs are available in the folder:

```
SasModeling/docs/sphinx-docs/build/html/user/models/model_functions.html
```

Run Tests:
----------

```
cd test
python run_one.py sasmodels/test/utest_models.py
```

*Note:*

```
test/run_one.py
```

needs:

```
run.py
```

Run all tests:

```
cd test
for i in `ls sasmodels/test/*.py`; do
  python run_one.py $i
  if [ $? -ne 0 ]; then
    echo "$* failed with exit code $?"
  fi
done
```


Notes:
------

Test:
```
cd test
python run_one.py sasmodels/test/utest_smearing.py
```
is not working as it needs SasView loaders. To make it work, SASview must be installed, e.g., as local library:
```
cd sasview-code
python setup.py install --user --record files.txt
```


