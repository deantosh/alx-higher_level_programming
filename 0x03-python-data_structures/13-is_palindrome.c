/*
 * Author: Deantosh M Daiddoh
 * File: 13-is_palindrome.c
 */

#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the linked list.
 *
 * Return: 1 (true) or 0 (false).
 */
int is_palindrome(listint_t **head)
{
	listint_t *current_ptr = *head;
	listint_t *reversed_ptr = reversed_list(head);

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/*start comparing values*/
	while (current_ptr && reversed_ptr)
	{
		if (current_ptr->n == reversed_ptr->n)
			continue;
		else
			return (0);

		current_ptr = current_ptr->next;
		reversed_ptr = reversed_ptr->next;
	}

	return (1);
}

/**
 * reversed_list - Reverses a singly linked list.
 * @head:  A pointer to the singly linked list.
 *
 * Return: A pointer to the singly linked list.
 */
listint_t *reversed_list(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL;
	listint_t *current = *head;

	while (!current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;

	return (*head);
}
