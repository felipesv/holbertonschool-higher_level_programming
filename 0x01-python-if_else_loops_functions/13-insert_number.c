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
	listint_t *new_list = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (new_list == NULL)
		return (NULL);

	(*new_list).n = number;
	(*new_list).next = NULL;

	if (*head == NULL)
	{
		*head = new_list;
		return (*head);
	}

	while (1)
	{

		if (current->next != NULL)
		{
			if (current->next->n > number)
			{
				new_list->next = current->next->next;
				current->next = new_list;
				return (new_list);
			}
		}
		else
		{
			current->next = new_list;
			return (new_list);
		}
		current = (*current).next;
	}
}
