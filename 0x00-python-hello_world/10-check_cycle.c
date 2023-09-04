#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: the list to be checked
 *
 * Return: 0 -> has no cycle
 * ------- 1 -> has  a cycle
*/
int check_cycle(listint_t *list)
{
	const listint_t *head = list;

	if (!list)
		return (0);

	list = list->next;

	while (list)
	{
		if (list == head)
			return (1);

		list = list->next;
	}

	return (0);
}
