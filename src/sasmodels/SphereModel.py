"""
Drop-in replacement for sasview cylinder model.

No rescaling or renaming of the parameters.
"""
from sasmodels.sasview_model import make_class
from sasmodels.models import sphere
SphereModel = make_class(sphere, dtype='single')

# use this? how?
from sasmodels.convert import convert_model

