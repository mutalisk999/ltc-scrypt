#include "Python.h"
#include "scrypt.h"

#define DEBUG_ASSERT(cond) \
if(!(cond)) \
{ \
    fprintf(stderr, "Assert: %s | Function: %s\n", #cond, __FUNCTION__); \
    assert(0); \
}

static PyObject* scrypt_1024_1_1_256_wrapper(PyObject *self, PyObject *args) {
    char* input_data;
    int input_data_len;
    char hash_data[32];
    char* p = (char*)hash_data;
    int hash_data_len = 32;

    DEBUG_ASSERT(args != NULL);
    PyArg_ParseTuple(args, "s#" , &input_data, &input_data_len);
    DEBUG_ASSERT(input_data != NULL);
    scrypt_1024_1_1_256(input_data, p);
    PyObject* resultObject = Py_BuildValue("s#", hash_data, hash_data_len);
    return resultObject;
}

static PyMethodDef ltc_scrypt_methods[] = {
    {"getPoWHash", scrypt_1024_1_1_256_wrapper, METH_VARARGS, "getPoWHash(input_data)"},
    {NULL, NULL, 0, NULL}
};

extern "C" {
    void initltc_scrypt(void) {
        Py_InitModule("ltc_scrypt", ltc_scrypt_methods);
    }
}
