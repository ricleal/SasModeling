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
   src/sans/models/include/DiamCyl.h
   AND RE-RUN THE GENERATOR SCRIPT
"""

from sans.models.BaseComponent import BaseComponent
from sans.models.sans_extension.c_models import CDiamCylFunc

def create_DiamCylFunc():
    """
       Create a model instance
    """
    obj = DiamCylFunc()
    # CDiamCylFunc.__init__(obj) is called by
    # the DiamCylFunc constructor
    return obj

class DiamCylFunc(CDiamCylFunc, BaseComponent):
    """ 
    Class that evaluates a DiamCylFunc model. 
    This file was auto-generated from src/sans/models/include/DiamCyl.h.
    Refer to that file and the structure it contains
    for details of the model.
    
    List of default parameters:

    * radius          = 20.0 A
    * length          = 400.0 A

    """
        
    def __init__(self, multfactor=1):
        """ Initialization """
        self.__dict__ = {}
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        #apply(CDiamCylFunc.__init__, (self,)) 

        CDiamCylFunc.__init__(self)
        self.is_multifunc = False
		        
        ## Name of the model
        self.name = "DiamCylFunc"
        ## Model description
        self.description = """
        To calculate the 2nd virial coefficient for
		the non-spherical object, then find the
		radius of sphere that has this value of
		virial coefficient.
        """
       
        ## Parameter details [units, min, max]
        self.details = {}
        self.details['radius'] = ['A', None, None]
        self.details['length'] = ['A', None, None]

        ## fittable parameters
        self.fixed = ['radius.width',
                      'length.width']
        
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
        return (create_DiamCylFunc, tuple(), state, None, None)
        
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(DiamCylFunc())   
       	
    def run(self, x=0.0):
        """ 
        Evaluate the model
        
        :param x: input q, or [q,phi]
        
        :return: scattering function P(q)
        
        """
        return CDiamCylFunc.run(self, x)
   
    def runXY(self, x=0.0):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q, or [qx, qy]
        
        :return: scattering function P(q)
        
        """
        return CDiamCylFunc.runXY(self, x)
        
    def evalDistribution(self, x):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q[], or [qx[], qy[]]
        
        :return: scattering function P(q[])
        
        """
        return CDiamCylFunc.evalDistribution(self, x)
        
    def calculate_ER(self):
        """ 
        Calculate the effective radius for P(q)*S(q)
        
        :return: the value of the effective radius
        
        """       
        return CDiamCylFunc.calculate_ER(self)
        
    def calculate_VR(self):
        """ 
        Calculate the volf ratio for P(q)*S(q)
        
        :return: the value of the volf ratio
        
        """       
        return CDiamCylFunc.calculate_VR(self)
              
    def set_dispersion(self, parameter, dispersion):
        """
        Set the dispersion object for a model parameter
        
        :param parameter: name of the parameter [string]
        :param dispersion: dispersion object of type DispersionModel
        
        """
        return CDiamCylFunc.set_dispersion(self,
               parameter, dispersion.cdisp)
        
   
# End of file
