#include "lists.h"
/**
 * insert_node - insert node
 * @head: head list
 * @number: number value
 *
 * Return: address
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_list = malloc(sizeof(listint_t)), *current = *head;

	if (new_list == NULL)
		return (NULL);

	(*new_list).n = number;

	if (*head == NULL)
	{
		(*new_list).next = NULL;
		*head = new_list;
		return (new_list);
	}

	if (current->n > number)
	{
		new_list->next = *head;
		*head = new_list;
		return (new_list);
	}

	while (current != NULL)
	{
		if (current->next != NULL && current->next->n > number)
		{
			new_list->next = current->next;
			current->next = new_list;
			break;
		}
		current = (*current).next;
	}
	current->next = new_list;
	return (new_list);
}
