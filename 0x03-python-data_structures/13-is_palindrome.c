#include "lists.h"

/**
 * add_nodeint - adds a new node at the start of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: duoble pointer to start of singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *b_half = NULL, *b_half_t = NULL;
	unsigned int len, i;

	if (!*head)
		return (1);
/* measure list */
	for (len = 0; temp; len++)
	{
		temp = temp->next;
	}
	temp = *head;

/* copy second half */
	for (i = 0; i < len; i++)
	{
		if (i >= (len - (len / 2)))
		{
			add_nodeint(&b_half, temp->n);
		}
		temp = temp->next;
	}
	temp = *head;
	b_half_t = b_half;

/* compare first half and reversed second half */
	for (i = 0; i < (len / 2); i++)
	{
		if (temp->n != b_half->n)
		{
			free_listint(b_half_t);
			return (0);
		}
		temp = temp->next;
		b_half = b_half->next;
	}

/* free second half */
	free_listint(b_half_t);
	return (1);
}
