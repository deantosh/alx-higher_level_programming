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
	listint_t *fast_ptr  = *head, *slow_ptr = *head;
	listint_t *second_half, *first_half = *head;

	/*if list is empty or has a single value*/
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast_ptr = fast_ptr->next->next; /*move twice*/
		/*if the list is even*/
		if (fast_ptr == NULL)
		{
			/*start of 2nd part of list*/
			second_half = slow_ptr->next;
			break;
		}
		/*if the list is odd*/
		if (fast_ptr->next == NULL)
		{
			/*start of the 2nd part of list*/
			second_half = slow_ptr->next->next;
			break;
		}
		slow_ptr = slow_ptr->next; /*move once*/
	}

	reversed_list(&second_half); /*reverse the second part of the list*/
	while (first_half && second_half)
	{
		if (first_half->n == second_half->n)
		{
			first_half = first_half->next;
			second_half = second_half->next;
		}
		else
			return (0);
	}
	if (second_half == NULL)
		return (1);
	return (0);
}

/**
 * reversed_list - Reverses a singly linked list.
 * @head:  A pointer to the singly linked list.
 *
 * Return: void.
 */
void reversed_list(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL;
	listint_t *current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
