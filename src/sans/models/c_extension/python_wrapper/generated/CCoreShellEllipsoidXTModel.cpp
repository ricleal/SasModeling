/**
	This software was developed by the University of Tennessee as part of the
	Distributed Data Analysis of Neutron Scattering Experiments (DANSE)
	project funded by the US National Science Foundation.

	If you use DANSE applications to do scientific research that leads to
	publication, we ask that you acknowledge the use of the software with the
	following sentence:

	"This work benefited from DANSE software developed under NSF award DMR-0520547."

	copyright 2008, University of Tennessee
 */

/** CCoreShellEllipsoidXTModel
 *
 * C extension 
 *
 * WARNING: THIS FILE WAS GENERATED BY WRAPPERGENERATOR.PY
 *          DO NOT MODIFY THIS FILE, MODIFY src/sans/models/include/spheroidXT.h
 *          AND RE-RUN THE GENERATOR SCRIPT
 *
 */
#define NO_IMPORT_ARRAY
#define PY_ARRAY_UNIQUE_SYMBOL PyArray_API_sans
 
extern "C" {
#include <Python.h>
#include <arrayobject.h>
#include "structmember.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

}

#include "spheroidXT.h"
#include "dispersion_visitor.hh"

/// Error object for raised exceptions
static PyObject * CCoreShellEllipsoidXTModelError = NULL;


// Class definition
typedef struct {
    PyObject_HEAD
    /// Parameters
    PyObject * params;
    /// Dispersion parameters
    PyObject * dispersion;
    /// Underlying model object
    CoreShellEllipsoidXTModel * model;
    /// Log for unit testing
    PyObject * log;
} CCoreShellEllipsoidXTModel;


static void
CCoreShellEllipsoidXTModel_dealloc(CCoreShellEllipsoidXTModel* self)
{
    Py_DECREF(self->params);
    Py_DECREF(self->dispersion);
    Py_DECREF(self->log);
    delete self->model;
    self->ob_type->tp_free((PyObject*)self);
    

}

static PyObject *
CCoreShellEllipsoidXTModel_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    CCoreShellEllipsoidXTModel *self;
    
    self = (CCoreShellEllipsoidXTModel *)type->tp_alloc(type, 0);
   
    return (PyObject *)self;
}

static int
CCoreShellEllipsoidXTModel_init(CCoreShellEllipsoidXTModel *self, PyObject *args, PyObject *kwds)
{
    if (self != NULL) {
    	
    	// Create parameters
        self->params = PyDict_New();
        self->dispersion = PyDict_New();

	self->model = new CoreShellEllipsoidXTModel();

        // Initialize parameter dictionary
        PyDict_SetItemString(self->params,"scale",Py_BuildValue("d",0.050000000000));
        PyDict_SetItemString(self->params,"sld_core",Py_BuildValue("d",0.000002000000));
        PyDict_SetItemString(self->params,"axis_theta",Py_BuildValue("d",0.000000000000));
        PyDict_SetItemString(self->params,"X_core",Py_BuildValue("d",3.000000000000));
        PyDict_SetItemString(self->params,"sld_solvent",Py_BuildValue("d",0.000006300000));
        PyDict_SetItemString(self->params,"T_shell",Py_BuildValue("d",30.000000000000));
        PyDict_SetItemString(self->params,"axis_phi",Py_BuildValue("d",0.000000000000));
        PyDict_SetItemString(self->params,"background",Py_BuildValue("d",0.001000000000));
        PyDict_SetItemString(self->params,"equat_core",Py_BuildValue("d",20.000000000000));
        PyDict_SetItemString(self->params,"XpolarShell",Py_BuildValue("d",1.000000000000));
        PyDict_SetItemString(self->params,"sld_shell",Py_BuildValue("d",0.000001000000));
        // Initialize dispersion / averaging parameter dict
        DispersionVisitor* visitor = new DispersionVisitor();
        PyObject * disp_dict;
        disp_dict = PyDict_New();
        self->model->equat_core.dispersion->accept_as_source(visitor, self->model->equat_core.dispersion, disp_dict);
        PyDict_SetItemString(self->dispersion, "equat_core", disp_dict);
        disp_dict = PyDict_New();
        self->model->X_core.dispersion->accept_as_source(visitor, self->model->X_core.dispersion, disp_dict);
        PyDict_SetItemString(self->dispersion, "X_core", disp_dict);
        disp_dict = PyDict_New();
        self->model->T_shell.dispersion->accept_as_source(visitor, self->model->T_shell.dispersion, disp_dict);
        PyDict_SetItemString(self->dispersion, "T_shell", disp_dict);
        disp_dict = PyDict_New();
        self->model->XpolarShell.dispersion->accept_as_source(visitor, self->model->XpolarShell.dispersion, disp_dict);
        PyDict_SetItemString(self->dispersion, "XpolarShell", disp_dict);
        disp_dict = PyDict_New();
        self->model->axis_phi.dispersion->accept_as_source(visitor, self->model->axis_phi.dispersion, disp_dict);
        PyDict_SetItemString(self->dispersion, "axis_phi", disp_dict);
        disp_dict = PyDict_New();
        self->model->axis_theta.dispersion->accept_as_source(visitor, self->model->axis_theta.dispersion, disp_dict);
        PyDict_SetItemString(self->dispersion, "axis_theta", disp_dict);


         
        // Create empty log
        self->log = PyDict_New();
        
        

    }
    return 0;
}

static char name_params[] = "params";
static char def_params[] = "Parameters";
static char name_dispersion[] = "dispersion";
static char def_dispersion[] = "Dispersion parameters";
static char name_log[] = "log";
static char def_log[] = "Log";

static PyMemberDef CCoreShellEllipsoidXTModel_members[] = {
    {name_params, T_OBJECT, offsetof(CCoreShellEllipsoidXTModel, params), 0, def_params},
	{name_dispersion, T_OBJECT, offsetof(CCoreShellEllipsoidXTModel, dispersion), 0, def_dispersion},     
    {name_log, T_OBJECT, offsetof(CCoreShellEllipsoidXTModel, log), 0, def_log},
    {NULL}  /* Sentinel */
};

/** Read double from PyObject
    @param p PyObject
    @return double
*/
double CCoreShellEllipsoidXTModel_readDouble(PyObject *p) {
    if (PyFloat_Check(p)==1) {
        return (double)(((PyFloatObject *)(p))->ob_fval);
    } else if (PyInt_Check(p)==1) {
        return (double)(((PyIntObject *)(p))->ob_ival);
    } else if (PyLong_Check(p)==1) {
        return (double)PyLong_AsLong(p);
    } else {
        return 0.0;
    }
}
/**
 * Function to call to evaluate model
 * @param args: input numpy array q[] 
 * @return: numpy array object 
 */
 
static PyObject *evaluateOneDim(CoreShellEllipsoidXTModel* model, PyArrayObject *q){
    PyArrayObject *result;
   
    // Check validity of array q , q must be of dimension 1, an array of double
    if (q->nd != 1 || q->descr->type_num != PyArray_DOUBLE)
    {
        //const char * message= "Invalid array: q->nd=%d,type_num=%d\n",q->nd,q->descr->type_num;
        //PyErr_SetString(PyExc_ValueError , message);
        return NULL;
    }
    result = (PyArrayObject *)PyArray_FromDims(q->nd, (int *)(q->dimensions), PyArray_DOUBLE);
	if (result == NULL) {
        const char * message= "Could not create result ";
        PyErr_SetString(PyExc_RuntimeError , message);
		return NULL;
	}
#pragma omp parallel for
	 for (int i = 0; i < q->dimensions[0]; i++){
      double q_value  = *(double *)(q->data + i*q->strides[0]);
      double *result_value = (double *)(result->data + i*result->strides[0]);
      *result_value =(*model)(q_value);
	}
    return PyArray_Return(result); 
 }

 /**
 * Function to call to evaluate model
 * @param args: input numpy array  [x[],y[]]
 * @return: numpy array object 
 */
 static PyObject * evaluateTwoDimXY( CoreShellEllipsoidXTModel* model, 
                              PyArrayObject *x, PyArrayObject *y)
 {
    PyArrayObject *result;
    int x_len, y_len, dims[1];
    //check validity of input vectors
    if (x->nd != 1 || x->descr->type_num != PyArray_DOUBLE
        || y->nd != 1 || y->descr->type_num != PyArray_DOUBLE
        || y->dimensions[0] != x->dimensions[0]){
        const char * message= "evaluateTwoDimXY  expect 2 numpy arrays";
        PyErr_SetString(PyExc_ValueError , message); 
        return NULL;
    }
   
	if (PyArray_Check(x) && PyArray_Check(y)) {
		
	    x_len = dims[0]= x->dimensions[0];
        y_len = dims[0]= y->dimensions[0];
	    
	    // Make a new double matrix of same dims
        result=(PyArrayObject *) PyArray_FromDims(1,dims,NPY_DOUBLE);
        if (result == NULL){
	    const char * message= "Could not create result ";
        PyErr_SetString(PyExc_RuntimeError , message);
	    return NULL;
	    }
       
        /* Do the calculation. */
#pragma omp parallel for
        for (int i=0; i< x_len; i++) {
            double x_value = *(double *)(x->data + i*x->strides[0]);
  		    double y_value = *(double *)(y->data + i*y->strides[0]);
  			double *result_value = (double *)(result->data +
  			      i*result->strides[0]);
  			*result_value = (*model)(x_value, y_value);
        }           
        return PyArray_Return(result); 
        
        }else{
		    PyErr_SetString(CCoreShellEllipsoidXTModelError, 
                   "CCoreShellEllipsoidXTModel.evaluateTwoDimXY couldn't run.");
	        return NULL;
		}      	
}
/**
 *  evalDistribution function evaluate a model function with input vector
 *  @param args: input q as vector or [qx, qy] where qx, qy are vectors
 *
 */ 
static PyObject * evalDistribution(CCoreShellEllipsoidXTModel *self, PyObject *args){
	PyObject *qx, *qy;
	PyArrayObject * pars;
	int npars ,mpars;
	
	// Get parameters
	
	    // Reader parameter dictionary
    self->model->scale = PyFloat_AsDouble( PyDict_GetItemString(self->params, "scale") );
    self->model->sld_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_core") );
    self->model->axis_theta = PyFloat_AsDouble( PyDict_GetItemString(self->params, "axis_theta") );
    self->model->X_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "X_core") );
    self->model->sld_solvent = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_solvent") );
    self->model->T_shell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "T_shell") );
    self->model->axis_phi = PyFloat_AsDouble( PyDict_GetItemString(self->params, "axis_phi") );
    self->model->background = PyFloat_AsDouble( PyDict_GetItemString(self->params, "background") );
    self->model->equat_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "equat_core") );
    self->model->XpolarShell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "XpolarShell") );
    self->model->sld_shell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_shell") );
    // Read in dispersion parameters
    PyObject* disp_dict;
    DispersionVisitor* visitor = new DispersionVisitor();
    disp_dict = PyDict_GetItemString(self->dispersion, "equat_core");
    self->model->equat_core.dispersion->accept_as_destination(visitor, self->model->equat_core.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "X_core");
    self->model->X_core.dispersion->accept_as_destination(visitor, self->model->X_core.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "T_shell");
    self->model->T_shell.dispersion->accept_as_destination(visitor, self->model->T_shell.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "XpolarShell");
    self->model->XpolarShell.dispersion->accept_as_destination(visitor, self->model->XpolarShell.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "axis_phi");
    self->model->axis_phi.dispersion->accept_as_destination(visitor, self->model->axis_phi.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "axis_theta");
    self->model->axis_theta.dispersion->accept_as_destination(visitor, self->model->axis_theta.dispersion, disp_dict);

	
	// Get input and determine whether we have to supply a 1D or 2D return value.
	if ( !PyArg_ParseTuple(args,"O",&pars) ) {
	    PyErr_SetString(CCoreShellEllipsoidXTModelError, 
	    	"CCoreShellEllipsoidXTModel.evalDistribution expects a q value.");
		return NULL;
	}
    // Check params
	
    if(PyArray_Check(pars)==1) {
		
	    // Length of list should 1 or 2
	    npars = pars->nd; 
	    if(npars==1) {
	        // input is a numpy array
	        if (PyArray_Check(pars)) {
		        return evaluateOneDim(self->model, (PyArrayObject*)pars); 
		    }
		}else{
		    PyErr_SetString(CCoreShellEllipsoidXTModelError, 
                   "CCoreShellEllipsoidXTModel.evalDistribution expect numpy array of one dimension.");
	        return NULL;
		}
    }else if( PyList_Check(pars)==1) {
    	// Length of list should be 2 for I(qx,qy)
	    mpars = PyList_GET_SIZE(pars); 
	    if(mpars!=2) {
	    	PyErr_SetString(CCoreShellEllipsoidXTModelError, 
	    		"CCoreShellEllipsoidXTModel.evalDistribution expects a list of dimension 2.");
	    	return NULL;
	    }
	     qx = PyList_GET_ITEM(pars,0);
	     qy = PyList_GET_ITEM(pars,1);
	     if (PyArray_Check(qx) && PyArray_Check(qy)) {
	         return evaluateTwoDimXY(self->model, (PyArrayObject*)qx,
		           (PyArrayObject*)qy);
		 }else{
		    PyErr_SetString(CCoreShellEllipsoidXTModelError, 
                   "CCoreShellEllipsoidXTModel.evalDistribution expect 2 numpy arrays in list.");
	        return NULL;
	     }
	}
	PyErr_SetString(CCoreShellEllipsoidXTModelError, 
                   "CCoreShellEllipsoidXTModel.evalDistribution couln't be run.");
	return NULL;
	
}

/**
 * Function to call to evaluate model
 * @param args: input q or [q,phi]
 * @return: function value
 */
static PyObject * run(CCoreShellEllipsoidXTModel *self, PyObject *args) {
	double q_value, phi_value;
	PyObject* pars;
	int npars;
	
	// Get parameters
	
	    // Reader parameter dictionary
    self->model->scale = PyFloat_AsDouble( PyDict_GetItemString(self->params, "scale") );
    self->model->sld_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_core") );
    self->model->axis_theta = PyFloat_AsDouble( PyDict_GetItemString(self->params, "axis_theta") );
    self->model->X_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "X_core") );
    self->model->sld_solvent = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_solvent") );
    self->model->T_shell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "T_shell") );
    self->model->axis_phi = PyFloat_AsDouble( PyDict_GetItemString(self->params, "axis_phi") );
    self->model->background = PyFloat_AsDouble( PyDict_GetItemString(self->params, "background") );
    self->model->equat_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "equat_core") );
    self->model->XpolarShell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "XpolarShell") );
    self->model->sld_shell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_shell") );
    // Read in dispersion parameters
    PyObject* disp_dict;
    DispersionVisitor* visitor = new DispersionVisitor();
    disp_dict = PyDict_GetItemString(self->dispersion, "equat_core");
    self->model->equat_core.dispersion->accept_as_destination(visitor, self->model->equat_core.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "X_core");
    self->model->X_core.dispersion->accept_as_destination(visitor, self->model->X_core.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "T_shell");
    self->model->T_shell.dispersion->accept_as_destination(visitor, self->model->T_shell.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "XpolarShell");
    self->model->XpolarShell.dispersion->accept_as_destination(visitor, self->model->XpolarShell.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "axis_phi");
    self->model->axis_phi.dispersion->accept_as_destination(visitor, self->model->axis_phi.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "axis_theta");
    self->model->axis_theta.dispersion->accept_as_destination(visitor, self->model->axis_theta.dispersion, disp_dict);

	
	// Get input and determine whether we have to supply a 1D or 2D return value.
	if ( !PyArg_ParseTuple(args,"O",&pars) ) {
	    PyErr_SetString(CCoreShellEllipsoidXTModelError, 
	    	"CCoreShellEllipsoidXTModel.run expects a q value.");
		return NULL;
	}
	  
	// Check params
	if( PyList_Check(pars)==1) {
		
		// Length of list should be 2 for I(q,phi)
	    npars = PyList_GET_SIZE(pars); 
	    if(npars!=2) {
	    	PyErr_SetString(CCoreShellEllipsoidXTModelError, 
	    		"CCoreShellEllipsoidXTModel.run expects a double or a list of dimension 2.");
	    	return NULL;
	    }
	    // We have a vector q, get the q and phi values at which
	    // to evaluate I(q,phi)
	    q_value = CCoreShellEllipsoidXTModel_readDouble(PyList_GET_ITEM(pars,0));
	    phi_value = CCoreShellEllipsoidXTModel_readDouble(PyList_GET_ITEM(pars,1));
	    // Skip zero
	    if (q_value==0) {
	    	return Py_BuildValue("d",0.0);
	    }
		return Py_BuildValue("d",(*(self->model)).evaluate_rphi(q_value,phi_value));

	} else {

		// We have a scalar q, we will evaluate I(q)
		q_value = CCoreShellEllipsoidXTModel_readDouble(pars);		
		
		return Py_BuildValue("d",(*(self->model))(q_value));
	}	
}
/**
 * Function to call to calculate_ER
 * @return: effective radius value 
 */
static PyObject * calculate_ER(CCoreShellEllipsoidXTModel *self) {

	// Get parameters
	
	    // Reader parameter dictionary
    self->model->scale = PyFloat_AsDouble( PyDict_GetItemString(self->params, "scale") );
    self->model->sld_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_core") );
    self->model->axis_theta = PyFloat_AsDouble( PyDict_GetItemString(self->params, "axis_theta") );
    self->model->X_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "X_core") );
    self->model->sld_solvent = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_solvent") );
    self->model->T_shell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "T_shell") );
    self->model->axis_phi = PyFloat_AsDouble( PyDict_GetItemString(self->params, "axis_phi") );
    self->model->background = PyFloat_AsDouble( PyDict_GetItemString(self->params, "background") );
    self->model->equat_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "equat_core") );
    self->model->XpolarShell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "XpolarShell") );
    self->model->sld_shell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_shell") );
    // Read in dispersion parameters
    PyObject* disp_dict;
    DispersionVisitor* visitor = new DispersionVisitor();
    disp_dict = PyDict_GetItemString(self->dispersion, "equat_core");
    self->model->equat_core.dispersion->accept_as_destination(visitor, self->model->equat_core.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "X_core");
    self->model->X_core.dispersion->accept_as_destination(visitor, self->model->X_core.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "T_shell");
    self->model->T_shell.dispersion->accept_as_destination(visitor, self->model->T_shell.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "XpolarShell");
    self->model->XpolarShell.dispersion->accept_as_destination(visitor, self->model->XpolarShell.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "axis_phi");
    self->model->axis_phi.dispersion->accept_as_destination(visitor, self->model->axis_phi.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "axis_theta");
    self->model->axis_theta.dispersion->accept_as_destination(visitor, self->model->axis_theta.dispersion, disp_dict);

		
	return Py_BuildValue("d",(*(self->model)).calculate_ER());

}
/**
 * Function to call to cal the ratio shell volume/ total volume
 * @return: the ratio shell volume/ total volume 
 */
static PyObject * calculate_VR(CCoreShellEllipsoidXTModel *self) {

	// Get parameters
	
	    // Reader parameter dictionary
    self->model->scale = PyFloat_AsDouble( PyDict_GetItemString(self->params, "scale") );
    self->model->sld_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_core") );
    self->model->axis_theta = PyFloat_AsDouble( PyDict_GetItemString(self->params, "axis_theta") );
    self->model->X_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "X_core") );
    self->model->sld_solvent = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_solvent") );
    self->model->T_shell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "T_shell") );
    self->model->axis_phi = PyFloat_AsDouble( PyDict_GetItemString(self->params, "axis_phi") );
    self->model->background = PyFloat_AsDouble( PyDict_GetItemString(self->params, "background") );
    self->model->equat_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "equat_core") );
    self->model->XpolarShell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "XpolarShell") );
    self->model->sld_shell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_shell") );
    // Read in dispersion parameters
    PyObject* disp_dict;
    DispersionVisitor* visitor = new DispersionVisitor();
    disp_dict = PyDict_GetItemString(self->dispersion, "equat_core");
    self->model->equat_core.dispersion->accept_as_destination(visitor, self->model->equat_core.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "X_core");
    self->model->X_core.dispersion->accept_as_destination(visitor, self->model->X_core.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "T_shell");
    self->model->T_shell.dispersion->accept_as_destination(visitor, self->model->T_shell.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "XpolarShell");
    self->model->XpolarShell.dispersion->accept_as_destination(visitor, self->model->XpolarShell.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "axis_phi");
    self->model->axis_phi.dispersion->accept_as_destination(visitor, self->model->axis_phi.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "axis_theta");
    self->model->axis_theta.dispersion->accept_as_destination(visitor, self->model->axis_theta.dispersion, disp_dict);

		
	return Py_BuildValue("d",(*(self->model)).calculate_VR());

}
/**
 * Function to call to evaluate model in cartesian coordinates
 * @param args: input q or [qx, qy]]
 * @return: function value
 */
static PyObject * runXY(CCoreShellEllipsoidXTModel *self, PyObject *args) {
	double qx_value, qy_value;
	PyObject* pars;
	int npars;
	
	// Get parameters
	
	    // Reader parameter dictionary
    self->model->scale = PyFloat_AsDouble( PyDict_GetItemString(self->params, "scale") );
    self->model->sld_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_core") );
    self->model->axis_theta = PyFloat_AsDouble( PyDict_GetItemString(self->params, "axis_theta") );
    self->model->X_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "X_core") );
    self->model->sld_solvent = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_solvent") );
    self->model->T_shell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "T_shell") );
    self->model->axis_phi = PyFloat_AsDouble( PyDict_GetItemString(self->params, "axis_phi") );
    self->model->background = PyFloat_AsDouble( PyDict_GetItemString(self->params, "background") );
    self->model->equat_core = PyFloat_AsDouble( PyDict_GetItemString(self->params, "equat_core") );
    self->model->XpolarShell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "XpolarShell") );
    self->model->sld_shell = PyFloat_AsDouble( PyDict_GetItemString(self->params, "sld_shell") );
    // Read in dispersion parameters
    PyObject* disp_dict;
    DispersionVisitor* visitor = new DispersionVisitor();
    disp_dict = PyDict_GetItemString(self->dispersion, "equat_core");
    self->model->equat_core.dispersion->accept_as_destination(visitor, self->model->equat_core.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "X_core");
    self->model->X_core.dispersion->accept_as_destination(visitor, self->model->X_core.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "T_shell");
    self->model->T_shell.dispersion->accept_as_destination(visitor, self->model->T_shell.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "XpolarShell");
    self->model->XpolarShell.dispersion->accept_as_destination(visitor, self->model->XpolarShell.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "axis_phi");
    self->model->axis_phi.dispersion->accept_as_destination(visitor, self->model->axis_phi.dispersion, disp_dict);
    disp_dict = PyDict_GetItemString(self->dispersion, "axis_theta");
    self->model->axis_theta.dispersion->accept_as_destination(visitor, self->model->axis_theta.dispersion, disp_dict);

	
	// Get input and determine whether we have to supply a 1D or 2D return value.
	if ( !PyArg_ParseTuple(args,"O",&pars) ) {
	    PyErr_SetString(CCoreShellEllipsoidXTModelError, 
	    	"CCoreShellEllipsoidXTModel.run expects a q value.");
		return NULL;
	}
	  
	// Check params
	if( PyList_Check(pars)==1) {
		
		// Length of list should be 2 for I(qx, qy))
	    npars = PyList_GET_SIZE(pars); 
	    if(npars!=2) {
	    	PyErr_SetString(CCoreShellEllipsoidXTModelError, 
	    		"CCoreShellEllipsoidXTModel.run expects a double or a list of dimension 2.");
	    	return NULL;
	    }
	    // We have a vector q, get the qx and qy values at which
	    // to evaluate I(qx,qy)
	    qx_value = CCoreShellEllipsoidXTModel_readDouble(PyList_GET_ITEM(pars,0));
	    qy_value = CCoreShellEllipsoidXTModel_readDouble(PyList_GET_ITEM(pars,1));
	    return Py_BuildValue("d",(*(self->model))(qx_value,qy_value));

	} else {

		// We have a scalar q, we will evaluate I(q)
		qx_value = CCoreShellEllipsoidXTModel_readDouble(pars);		
		
		return Py_BuildValue("d",(*(self->model))(qx_value));
	}	
}

static PyObject * reset(CCoreShellEllipsoidXTModel *self, PyObject *args) {
    

    return Py_BuildValue("d",0.0);
}

static PyObject * set_dispersion(CCoreShellEllipsoidXTModel *self, PyObject *args) {
	PyObject * disp;
	const char * par_name;

	if ( !PyArg_ParseTuple(args,"sO", &par_name, &disp) ) {
	    PyErr_SetString(CCoreShellEllipsoidXTModelError,
	    	"CCoreShellEllipsoidXTModel.set_dispersion expects a DispersionModel object.");
		return NULL;
	}
	void *temp = PyCObject_AsVoidPtr(disp);
	DispersionModel * dispersion = static_cast<DispersionModel *>(temp);


	// Ugliness necessary to go from python to C
	    // TODO: refactor this
    if (!strcmp(par_name, "equat_core")) {
        self->model->equat_core.dispersion = dispersion;
    } else    if (!strcmp(par_name, "X_core")) {
        self->model->X_core.dispersion = dispersion;
    } else    if (!strcmp(par_name, "T_shell")) {
        self->model->T_shell.dispersion = dispersion;
    } else    if (!strcmp(par_name, "XpolarShell")) {
        self->model->XpolarShell.dispersion = dispersion;
    } else    if (!strcmp(par_name, "axis_phi")) {
        self->model->axis_phi.dispersion = dispersion;
    } else    if (!strcmp(par_name, "axis_theta")) {
        self->model->axis_theta.dispersion = dispersion;
    } else {
	    PyErr_SetString(CCoreShellEllipsoidXTModelError,
	    	"CCoreShellEllipsoidXTModel.set_dispersion expects a valid parameter name.");
		return NULL;
	}

	DispersionVisitor* visitor = new DispersionVisitor();
	PyObject * disp_dict = PyDict_New();
	dispersion->accept_as_source(visitor, dispersion, disp_dict);
	PyDict_SetItemString(self->dispersion, par_name, disp_dict);
    return Py_BuildValue("i",1);
}


static PyMethodDef CCoreShellEllipsoidXTModel_methods[] = {
    {"run",      (PyCFunction)run     , METH_VARARGS,
      "Evaluate the model at a given Q or Q, phi"},
    {"runXY",      (PyCFunction)runXY     , METH_VARARGS,
      "Evaluate the model at a given Q or Qx, Qy"},
    {"calculate_ER",      (PyCFunction)calculate_ER     , METH_VARARGS,
      "Evaluate the model at a given Q or Q, phi"},
    {"calculate_VR",      (PyCFunction)calculate_VR     , METH_VARARGS,
      "Evaluate VR"},    
    {"evalDistribution",  (PyCFunction)evalDistribution , METH_VARARGS,
      "Evaluate the model at a given Q or Qx, Qy vector "},
    {"reset",    (PyCFunction)reset   , METH_VARARGS,
      "Reset pair correlation"},
    {"set_dispersion",      (PyCFunction)set_dispersion     , METH_VARARGS,
      "Set the dispersion model for a given parameter"},
   {NULL}
};

static PyTypeObject CCoreShellEllipsoidXTModelType = {
    PyObject_HEAD_INIT(NULL)
    0,                         /*ob_size*/
    "CCoreShellEllipsoidXTModel",             /*tp_name*/
    sizeof(CCoreShellEllipsoidXTModel),             /*tp_basicsize*/
    0,                         /*tp_itemsize*/
    (destructor)CCoreShellEllipsoidXTModel_dealloc, /*tp_dealloc*/
    0,                         /*tp_print*/
    0,                         /*tp_getattr*/
    0,                         /*tp_setattr*/
    0,                         /*tp_compare*/
    0,                         /*tp_repr*/
    0,                         /*tp_as_number*/
    0,                         /*tp_as_sequence*/
    0,                         /*tp_as_mapping*/
    0,                         /*tp_hash */
    0,                         /*tp_call*/
    0,                         /*tp_str*/
    0,                         /*tp_getattro*/
    0,                         /*tp_setattro*/
    0,                         /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /*tp_flags*/
    "CCoreShellEllipsoidXTModel objects",           /* tp_doc */
    0,		               /* tp_traverse */
    0,		               /* tp_clear */
    0,		               /* tp_richcompare */
    0,		               /* tp_weaklistoffset */
    0,		               /* tp_iter */
    0,		               /* tp_iternext */
    CCoreShellEllipsoidXTModel_methods,             /* tp_methods */
    CCoreShellEllipsoidXTModel_members,             /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)CCoreShellEllipsoidXTModel_init,      /* tp_init */
    0,                         /* tp_alloc */
    CCoreShellEllipsoidXTModel_new,                 /* tp_new */
};


//static PyMethodDef module_methods[] = {
//    {NULL} 
//};

/**
 * Function used to add the model class to a module
 * @param module: module to add the class to
 */ 
void addCCoreShellEllipsoidXTModel(PyObject *module) {
	PyObject *d;
	
    if (PyType_Ready(&CCoreShellEllipsoidXTModelType) < 0)
        return;

    Py_INCREF(&CCoreShellEllipsoidXTModelType);
    PyModule_AddObject(module, "CCoreShellEllipsoidXTModel", (PyObject *)&CCoreShellEllipsoidXTModelType);
    
    d = PyModule_GetDict(module);
    static char error_name[] = "CCoreShellEllipsoidXTModel.error";
    CCoreShellEllipsoidXTModelError = PyErr_NewException(error_name, NULL, NULL);
    PyDict_SetItemString(d, "CCoreShellEllipsoidXTModelError", CCoreShellEllipsoidXTModelError);
}
