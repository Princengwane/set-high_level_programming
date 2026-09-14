#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints info about Python bytes objects
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i, limit;
char *string;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = ((PyVarObject *)p)->ob_size;
string = ((PyBytesObject *)p)->ob_sval;

printf("  size: %zd\n", size);
printf("  trying string: %s\n", string);

limit = size >= 10 ? 10 : size + 1;
printf("  first %zd bytes:", limit);

for (i = 0; i < limit; i++)
{
printf(" %02hhx", string[i]);
}
printf("\n");
}

/**
 * print_python_list - Prints info about Python lists
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, allocated, i;
PyObject *item;
PyListObject *list = (PyListObject *)p;

if (!PyList_Check(p))
return;

size = list->ob_base.ob_size;
allocated = list->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", allocated);

for (i = 0; i < size; i++)
{
item = list->ob_item[i];
printf("Element %zd: %s\n", i, item->ob_type->tp_name);
if (PyBytes_Check(item))
print_python_bytes(item);
}
}
