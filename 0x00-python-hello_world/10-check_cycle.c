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
/*	int i = 0, j = 0; */

	if (!list)
		return (-1);

	base = list;
	test = list;

/*	printf("base before loop: %p\n", (void *)base); */
/*	printf("test before loop: %p\n", (void *)test); */

	while (base->next)
	{
/*		printf("base: %p loop: %i\n", (void *)base, i); */
		while (test->next)
		{
/*			printf("___test: %p loop: %i\n", (void *)test->next, j); */
			if (test->next == base)
				return (1);
			test = test->next;
/*			j++; */
		}
/*		j = 0; */
		base = base->next;
		test = base;
/*		i++; */
	}

	return (0);
}
