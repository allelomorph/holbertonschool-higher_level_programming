#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks singly linked list type listint_t for backward links
 *
 * @list: point in a singly linked list to begin search for backward links
 *
 * Return: 0 if all links move forward through list, 1 if backward link
 *         is found, or -1 on failure
 */

int check_cycle(listint_t *list)
{
	listint_t *base, *test;

	base = list;
	test = list;

	while (base && test && test->next)
	{
		base = base->next;
		test = test->next->next;
		if (base == test)
			return (1);
	}
	return (0);
}
