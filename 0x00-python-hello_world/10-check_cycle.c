/*
 * Author: Deantosh M Daiddoh
 * File: 10-check_cycle.c
 */

#include "lists.h"

/**
 * check_cycle - Checks if a linked list is cyclic.
 * @list: The linked list to test.
 *
 * Return: 1 (true) or 0 (fails).
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list, *fast_ptr  = list;

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next; /*move once*/
		fast_ptr = fast_ptr->next->next; /*move twice*/
		if (slow_ptr == fast_ptr) /*cyclic*/
			return (1);
	}
	return (0); /*not cyclic*/
}
