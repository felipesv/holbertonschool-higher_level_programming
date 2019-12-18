#include "lists.h"
/**
 * is_palindrome - singly linked list is a palindrome.
 * @head: head
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int is_palindrome(listint_t **head)
{
	listint_t *c1 = *head, *c2 = *head;
	int sizeL = 0, i, middle = 0;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	while (c2->next != NULL)
	{
		c2 = c2->next;
		sizeL++;
	}

	middle = sizeL / 2;

	while (c1 != NULL && c2 != NULL)
	{
		if (c1->n != c2->n)
			return (0);

		c2 = *head;
		for (i = 0; i < (sizeL - 1); i++)
			c2 = c2->next;

		sizeL = sizeL - 1;

		if (middle == sizeL)
			break;

		c1 = c1->next;
	}
	return (1);

}
