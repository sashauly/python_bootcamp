#include <Python.h>

static PyObject *add(PyObject *self, PyObject *args)
{
    PyObject *a_obj;
    PyObject *b_obj;
    double a, b;

    if (!PyArg_ParseTuple(args, "OO", &a_obj, &b_obj))
    {
        return NULL;
    }

    if (PyLong_Check(a_obj) && PyLong_Check(b_obj))
    {
        a = PyLong_AsDouble(a_obj);
        b = PyLong_AsDouble(b_obj);
    }
    else if (PyFloat_Check(a_obj) && PyFloat_Check(b_obj))
    {
        a = PyFloat_AsDouble(a_obj);
        b = PyFloat_AsDouble(b_obj);
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "Invalid argument types");
        return NULL;
    }

    return PyFloat_FromDouble(a + b);
}

static PyObject *sub(PyObject *self, PyObject *args)
{
    PyObject *a_obj;
    PyObject *b_obj;
    double a, b;

    if (!PyArg_ParseTuple(args, "OO", &a_obj, &b_obj))
    {
        return NULL;
    }

    if (PyLong_Check(a_obj) && PyLong_Check(b_obj))
    {
        a = PyLong_AsDouble(a_obj);
        b = PyLong_AsDouble(b_obj);
    }
    else if (PyFloat_Check(a_obj) && PyFloat_Check(b_obj))
    {
        a = PyFloat_AsDouble(a_obj);
        b = PyFloat_AsDouble(b_obj);
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "Invalid argument types");
        return NULL;
    }

    return PyFloat_FromDouble(a - b);
}

static PyObject *mul(PyObject *self, PyObject *args)
{
    PyObject *a_obj;
    PyObject *b_obj;
    double a, b;

    if (!PyArg_ParseTuple(args, "OO", &a_obj, &b_obj))
    {
        return NULL;
    }

    if (PyLong_Check(a_obj) && PyLong_Check(b_obj))
    {
        a = PyLong_AsDouble(a_obj);
        b = PyLong_AsDouble(b_obj);
    }
    else if (PyFloat_Check(a_obj) && PyFloat_Check(b_obj))
    {
        a = PyFloat_AsDouble(a_obj);
        b = PyFloat_AsDouble(b_obj);
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "Invalid argument types");
        return NULL;
    }

    return PyFloat_FromDouble(a * b);
}

static PyObject *division(PyObject *self, PyObject *args)
{
    PyObject *a_obj;
    PyObject *b_obj;
    double a, b;

    if (!PyArg_ParseTuple(args, "OO", &a_obj, &b_obj))
    {
        return NULL;
    }

    if (PyLong_Check(a_obj) && PyLong_Check(b_obj))
    {
        a = PyLong_AsDouble(a_obj);
        b = PyLong_AsDouble(b_obj);
    }
    else if (PyFloat_Check(a_obj) && PyFloat_Check(b_obj))
    {
        a = PyFloat_AsDouble(a_obj);
        b = PyFloat_AsDouble(b_obj);
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "Invalid argument types");
        return NULL;
    }

    if (b == 0)
    {
        PyErr_SetString(PyExc_ZeroDivisionError, "Cannot divide by zero");
        return NULL;
    }

    return PyFloat_FromDouble(a / b);
}

static PyMethodDef CalculatorMethods[] = {
    {"add", add, METH_VARARGS, "Add two numbers."},
    {"sub", sub, METH_VARARGS, "Subtract two numbers."},
    {"mul", mul, METH_VARARGS, "Multiply two numbers."},
    {"div", division, METH_VARARGS, "Divide two numbers."},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef calculatormodule = {
    PyModuleDef_HEAD_INIT,
    "calculator",
    "Python module that provides basic calculator functions",
    -1,
    CalculatorMethods};

PyMODINIT_FUNC PyInit_calculator(void)
{
    return PyModule_Create(&calculatormodule);
}
