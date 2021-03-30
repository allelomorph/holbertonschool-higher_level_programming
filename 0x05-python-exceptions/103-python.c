/* printf fflush */
#include <stdio.h>
/* strchr */
#include <string.h>
/* Python C API */
#include <Python.h>


/**
 * print_python_bytes - prints the size, string representation, and hex
 * representation of a Python bytes object
 *
 * Some cpython macros/functions prohibited by project task instructions.
 *
 * @p: PyObject *-castable struct pointer
 */
void print_python_bytes(PyObject *p)
{
	int i;
	Py_ssize_t size, printed_bytes;
	char *array_as_string = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	printf("  size: %li\n", size);

	array_as_string = ((PyBytesObject *)(p))->ob_sval;
	printf("  trying string: %s\n", array_as_string);

	printed_bytes = (size + 1 >= 10) ? 10 : size + 1;
	printf("  first %li bytes:", printed_bytes);
	for (i = 0; i < printed_bytes; i++)
		printf(" %02x", (unsigned char)(array_as_string[i]));
	putchar('\n');
	fflush(stdout);
}


/**
 * print_python_float - prints value of a Python float object: at least one
 * place of precision, no trailing zeroes
 *
 * Some cpython macros/functions prohibited by project task instructions.
 *
 * @p: PyObject *-castable struct pointer
 */
void print_python_float(PyObject *p)
{
	char float_str[40];

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}

	/*
	 * Could not find printf format tag that accommodated both variable
	 * precision with no trailing zeroes AND .0 for integers
	 */
	sprintf(float_str, "%.16g", ((PyFloatObject *)p)->ob_fval);
	if (strchr(float_str, '.') != NULL)
		printf("  value: %s\n", float_str);
	else
		printf("  value: %.1f\n", ((PyFloatObject *)p)->ob_fval);

	fflush(stdout);
}


/**
 * print_python_list - prints member count, allocated spaces, and member
 * element types for python lists
 *
 * Some cpython macros/functions prohibited by project task instructions.
 *
 * @p: PyObject *-castable struct pointer
 */
void print_python_list(PyObject *p)
{
	int i;
	Py_ssize_t size;
	PyObject *list_member;

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}

	printf("[*] Python list info\n");

	size = ((PyVarObject *)(p))->ob_size;
	printf("[*] Size of the Python List = %li\n", size);

	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		list_member = ((PyListObject *)p)->ob_item[i];
		printf("Element %d: %s\n", i,
		       list_member->ob_type->tp_name);

		if (PyBytes_Check(list_member))
			print_python_bytes(list_member);
		else if (PyFloat_Check(list_member))
			print_python_float(list_member);

	}
	fflush(stdout);
}
