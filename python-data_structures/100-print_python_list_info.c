#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: PyObject pointer to Python list
 */
void print_python_list_info(PyObject *p)
{
Py_ssize_t size, allocated, i;
PyObject *item;
PyListObject *list = (PyListObject *)p;

size = PyList_Size(p);
allocated = list->allocated;

printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}
