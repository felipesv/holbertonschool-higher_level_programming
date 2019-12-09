#include "lists.h"
/**
 * check_cycle - Linked list cycle
 * @list: head
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *list_1, *list_2;

	list_1 = list;
	list_2 = list;

	while (list_1 != NULL && list_2 != NULL && list_2->next != NULL)
	{
		list_1 = list_1->next;
		list_2 = list_2->next->next;

		if (list_1 == list_2)
		{
			return (1);
		}
	}

	return (0);
}
