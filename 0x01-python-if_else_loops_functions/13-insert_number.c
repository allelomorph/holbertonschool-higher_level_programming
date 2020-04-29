#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - prints all elements of a listint_t list
 * @head: double pointer to head of list
 * @number: integer to be stored in new node
 * Return: pointer to new node, or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (!head)
	{
		new->next = NULL;
		return (new);
	}

	curr = *head;

	while (curr->next && curr->next->n < number)
	{
		curr = curr->next;
	}

	if (curr->n < number)
	{
		new->next = curr->next;
		curr->next = new;
	}
	else
	{
		new->next = curr;
		*head = new;
	}

	return (new);
}
