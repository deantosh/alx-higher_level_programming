/*
 * Author: Deantosh M Daiddoh
 * File: 100-print_python_list_info.c
 */

#include <Python.h>
#include <listobject.h>
#include <object.h>

/*include function prototype*/
void print_python_list_info(PyObject *p);

/**
 * print_python_list_info - Prints information about python lists.
 * @p: The python object containing the list.
 *
 * Return: void.
 */
void print_python_list_info(PyObject *p)
{
	long int list_size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p; /*cast*/
	int i = 0;

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", obj->allocated);

	/*loop though list to print items*/
	while (i < list_size)
	{
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
		i++;
	}
}
