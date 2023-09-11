#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * rev_listint - reverses a linked list
 * @head: pointer to the list
 *
 * Return: pointer to first node of the new list
 */
void rev_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks whether a list is a palindrome
 * @head: pointer to pointer to list
 *
 * Return: 1 -> if palindrome
 * ------- 0 -> if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *temp = *head, *copy = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			copy = slow->next;
			break;
		}
		if (!fast->next)
		{
			copy = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	rev_listint(&copy);

	while (copy && temp)
	{
		if (temp->n == copy->n)
		{
			copy = copy->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!copy)
		return (1);

	return (0);
}
