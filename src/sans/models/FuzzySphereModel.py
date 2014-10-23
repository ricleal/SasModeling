##############################################################################
# This software was developed by the University of Tennessee as part of the
# Distributed Data Analysis of Neutron Scattering Experiments (DANSE)
# project funded by the US National Science Foundation.
#
# If you use DANSE applications to do scientific research that leads to
# publication, we ask that you acknowledge the use of the software with the
# following sentence:
#
# This work benefited from DANSE software developed under NSF award DMR-0520547
#
# Copyright 2008-2011, University of Tennessee
##############################################################################

""" 
Provide functionality for a C extension model

.. WARNING::

   THIS FILE WAS GENERATED BY WRAPPERGENERATOR.PY
   DO NOT MODIFY THIS FILE, MODIFY
   src/sans/models/include/fuzzysphere.h
   AND RE-RUN THE GENERATOR SCRIPT
"""

from sans.models.BaseComponent import BaseComponent
from sans.models.sans_extension.c_models import CFuzzySphereModel

def create_FuzzySphereModel():
    """
       Create a model instance
    """
    obj = FuzzySphereModel()
    # CFuzzySphereModel.__init__(obj) is called by
    # the FuzzySphereModel constructor
    return obj

class FuzzySphereModel(CFuzzySphereModel, BaseComponent):
    """ 
    Class that evaluates a FuzzySphereModel model. 
    This file was auto-generated from src/sans/models/include/fuzzysphere.h.
    Refer to that file and the structure it contains
    for details of the model.
    
    List of default parameters:

    * radius          = 60.0 [A]
    * scale           = 0.01 
    * fuzziness       = 10.0 [A]
    * sldSph          = 1e-06 [1/A^(2)]
    * sldSolv         = 3e-06 [1/A^(2)]
    * background      = 0.001 [1/cm]

    """
        
    def __init__(self, multfactor=1):
        """ Initialization """
        self.__dict__ = {}
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        #apply(CFuzzySphereModel.__init__, (self,)) 

        CFuzzySphereModel.__init__(self)
        self.is_multifunc = False
		        
        ## Name of the model
        self.name = "FuzzySphereModel"
        ## Model description
        self.description = """
        
		scale: scale factor times volume fraction,
		or just volume fraction for absolute scale data
		radius: radius of the solid sphere
		fuzziness = the STD of the height of fuzzy interfacial
		thickness (ie., so-called interfacial roughness)
		sldSph: the SLD of the sphere
		sldSolv: the SLD of the solvent
		background: incoherent background
		Note: By definition, this function works only when fuzziness << radius.
        """
       
        ## Parameter details [units, min, max]
        self.details = {}
        self.details['radius'] = ['[A]', None, None]
        self.details['scale'] = ['', None, None]
        self.details['fuzziness'] = ['[A]', None, None]
        self.details['sldSph'] = ['[1/A^(2)]', None, None]
        self.details['sldSolv'] = ['[1/A^(2)]', None, None]
        self.details['background'] = ['[1/cm]', None, None]

        ## fittable parameters
        self.fixed = ['radius.width',
                      'fuzziness.width']
        
        ## non-fittable parameters
        self.non_fittable = []
        
        ## parameters with orientation
        self.orientation_params = []

        ## parameters with magnetism
        self.magnetic_params = []

        self.category = None
        self.multiplicity_info = None
        
    def __setstate__(self, state):
        """
        restore the state of a model from pickle
        """
        self.__dict__, self.params, self.dispersion = state
        
    def __reduce_ex__(self, proto):
        """
        Overwrite the __reduce_ex__ of PyTypeObject *type call in the init of 
        c model.
        """
        state = (self.__dict__, self.params, self.dispersion)
        return (create_FuzzySphereModel, tuple(), state, None, None)
        
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(FuzzySphereModel())   
       	
    def run(self, x=0.0):
        """ 
        Evaluate the model
        
        :param x: input q, or [q,phi]
        
        :return: scattering function P(q)
        
        """
        return CFuzzySphereModel.run(self, x)
   
    def runXY(self, x=0.0):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q, or [qx, qy]
        
        :return: scattering function P(q)
        
        """
        return CFuzzySphereModel.runXY(self, x)
        
    def evalDistribution(self, x):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q[], or [qx[], qy[]]
        
        :return: scattering function P(q[])
        
        """
        return CFuzzySphereModel.evalDistribution(self, x)
        
    def calculate_ER(self):
        """ 
        Calculate the effective radius for P(q)*S(q)
        
        :return: the value of the effective radius
        
        """       
        return CFuzzySphereModel.calculate_ER(self)
        
    def calculate_VR(self):
        """ 
        Calculate the volf ratio for P(q)*S(q)
        
        :return: the value of the volf ratio
        
        """       
        return CFuzzySphereModel.calculate_VR(self)
              
    def set_dispersion(self, parameter, dispersion):
        """
        Set the dispersion object for a model parameter
        
        :param parameter: name of the parameter [string]
        :param dispersion: dispersion object of type DispersionModel
        
        """
        return CFuzzySphereModel.set_dispersion(self,
               parameter, dispersion.cdisp)
        
   
# End of file

