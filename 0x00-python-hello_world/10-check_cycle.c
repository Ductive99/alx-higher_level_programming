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
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	list = list->next;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
