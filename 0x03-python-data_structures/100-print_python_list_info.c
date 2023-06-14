#include <Python.h>
#include <stdio.h>

/**
* print_python_list_info - print python list info from c file
* @p: pyton list
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, sz = PyList_Size(p);
	PyObject *element;
	const char *type_name;

	printf("[*] Size of the Python List = %zd\n", sz);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < sz; i++)
	{
		element = PyList_GetItem(p, i);
		type_name = Py_TYPE(element)->tp_name;
		printf("Element %zd: %s\n", i, type_name);

	}
}
