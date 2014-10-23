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
   src/sans/models/include/FractalQtoN.h
   AND RE-RUN THE GENERATOR SCRIPT
"""

from sans.models.BaseComponent import BaseComponent
from sans.models.sans_extension.c_models import CFractalO_Z

def create_FractalO_Z():
    """
       Create a model instance
    """
    obj = FractalO_Z()
    # CFractalO_Z.__init__(obj) is called by
    # the FractalO_Z constructor
    return obj

class FractalO_Z(CFractalO_Z, BaseComponent):
    """ 
    Class that evaluates a FractalO_Z model. 
    This file was auto-generated from src/sans/models/include/FractalQtoN.h.
    Refer to that file and the structure it contains
    for details of the model.
    
    List of default parameters:

    * scale           = 10000.0 
    * m_fractal       = 1.8 
    * cluster_rg      = 3520.0 
    * s_fractal       = 2.5 
    * primary_rg      = 82.0 
    * background      = 0.01 

    """
        
    def __init__(self, multfactor=1):
        """ Initialization """
        self.__dict__ = {}
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        #apply(CFractalO_Z.__init__, (self,)) 

        CFractalO_Z.__init__(self)
        self.is_multifunc = False
		        
        ## Name of the model
        self.name = "FractalO_Z"
        ## Model description
        self.description = """
        Structure factor for interacting particles:
		Schmidt J Appl Cryst (1991), 24, 414-435 See equation (19)
		Hurd; Schaefer; Martin, Phys Rev A (1987), 35, 2361-2364 See equation (2).
        """
       
        ## Parameter details [units, min, max]
        self.details = {}
        self.details['scale'] = ['', None, None]
        self.details['m_fractal'] = ['', None, None]
        self.details['cluster_rg'] = ['', None, None]
        self.details['s_fractal'] = ['', None, None]
        self.details['primary_rg'] = ['', None, None]
        self.details['background'] = ['', None, None]

        ## fittable parameters
        self.fixed = []
        
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
        return (create_FractalO_Z, tuple(), state, None, None)
        
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(FractalO_Z())   
       	
    def run(self, x=0.0):
        """ 
        Evaluate the model
        
        :param x: input q, or [q,phi]
        
        :return: scattering function P(q)
        
        """
        return CFractalO_Z.run(self, x)
   
    def runXY(self, x=0.0):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q, or [qx, qy]
        
        :return: scattering function P(q)
        
        """
        return CFractalO_Z.runXY(self, x)
        
    def evalDistribution(self, x):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q[], or [qx[], qy[]]
        
        :return: scattering function P(q[])
        
        """
        return CFractalO_Z.evalDistribution(self, x)
        
    def calculate_ER(self):
        """ 
        Calculate the effective radius for P(q)*S(q)
        
        :return: the value of the effective radius
        
        """       
        return CFractalO_Z.calculate_ER(self)
        
    def calculate_VR(self):
        """ 
        Calculate the volf ratio for P(q)*S(q)
        
        :return: the value of the volf ratio
        
        """       
        return CFractalO_Z.calculate_VR(self)
              
    def set_dispersion(self, parameter, dispersion):
        """
        Set the dispersion object for a model parameter
        
        :param parameter: name of the parameter [string]
        :param dispersion: dispersion object of type DispersionModel
        
        """
        return CFractalO_Z.set_dispersion(self,
               parameter, dispersion.cdisp)
        
   
# End of file

