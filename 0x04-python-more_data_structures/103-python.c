#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
* print_python_bytes - print python list info from c file
* @p: pyton list
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t sz;
	const char *type_name;

	printf("[.] bytes object info\n");

	type_name = Py_TYPE(p)->tp_name;
	if (strcmp(type_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	sz = PyBytes_Size(p);
	printf("  size: %zd\n", sz);
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %zd bytes:\n", sz + 1);
}
/**
* print_python_list - print python list info from c file
* @p: pyton list
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t i, sz = PyList_Size(p);
	PyObject *element;
	const char *type_name;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", sz);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < sz; i++)
	{
		element = PyList_GetItem(p, i);
		type_name = Py_TYPE(element)->tp_name;
		printf("Element %zd: %s\n", i, type_name);
		if (strcmp(type_name, "bytes") == 0)
			print_python_bytes(element);
	}
}
