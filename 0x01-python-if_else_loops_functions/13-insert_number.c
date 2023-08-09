/*
 * Author: Deantosh M Daiddoh
 * File: 13-insert_number.c
 */

#include "lists.h"

/**
 * insert_node - Inserts a node in a sorted singly linked list.
 * @head: A pointer to the linked list.
 * @number: The data to add to the list.
 *
 * Return: A pointer to the new linked list.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new_node;
	listint_t *prev_node;
	int index, idx = 0;

	current = *head;
	/*get node whose value is bigger than number*/
	while (current != NULL)
	{
		if (current->n > number)
			break;
		current = current->next;/*move ptr*/
		idx++;
	}

	/*allocate memory*/
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/*add data*/
	new_node->n = number;

	/*get previous node*/
	prev_node = *head;
	for (index = 0; index < (idx - 1); index++)
	{
		if (prev_node->next == NULL)
			return (NULL);
		prev_node = prev_node->next;
	}
	new_node->next = prev_node->next;
	prev_node->next = new_node;
	return (new_node);
}
