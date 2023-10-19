#include <Python.h>
#include <math.h>

/*  �������Ϻ���cos_func */
static PyObject* cos_func(PyObject* self, PyObject* args)
{
    double value;
    double answer;

    if (!PyArg_ParseTuple(args, "d", &value))
        return NULL;
 
       answer = cos(value);
   
    return Py_BuildValue("f", answer);
}

/*  ����ģ�巽������ */
static PyMethodDef CosMethods[] =
{
     {"cos_func", cos_func, METH_VARARGS, "evaluate the cosine"},
     {NULL, NULL, 0, NULL}
};

#if PY_MAJOR_VERSION >= 3
/* ��Python3�����³�ʼ������ģ�� */
/* Python version 3*/
static struct PyModuleDef cModPyDem =
{
    PyModuleDef_HEAD_INIT,
    "cos_module", "Some documentation",
    -1,
    CosMethods
};

PyMODINIT_FUNC
PyInit_cos_module(void)
{
    return PyModule_Create(&cModPyDem);
}

#else

/* ��Python2�����³�ʼ������ģ�� */
/* Python version 2 */
PyMODINIT_FUNC
initcos_module(void)
{
    (void) Py_InitModule("cos_module", CosMethods);
}

#endif

