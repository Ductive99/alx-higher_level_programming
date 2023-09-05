#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a new node in a listint_t list
 * @head: pointer to pointer of first node of the list
 * @number: integer to be included in the new node
 *
 * Return: address of the new element or NULL if it fails
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if (current->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (current->next)
		{
			if (current->next->n >= number)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			current = current->next;
		}
	}

	add_nodeint_end(head, number);

	return (new);
}
