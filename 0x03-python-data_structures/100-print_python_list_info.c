#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints list info on python
 * @p: pyobject pointer
 *
 * Return: void
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t count;
	Py_ssize_t size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %ld\n", obj->allocated);

	for (count = 0; count < size; count++)
		printf("Element %ld: %s\n", count, Py_TYPE(obj->ob_item[count])->tp_name);

}
