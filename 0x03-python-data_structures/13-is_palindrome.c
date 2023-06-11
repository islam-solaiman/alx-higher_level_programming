#include "lists.h"

/**
 * reverse_list - function reverses linked list
 * @h1: list to be reverses
 * @h2: reversed linked kist
 */
void reverse_list(listint_t *h1, listint_t **h2)
{
	if (h1 == NULL)
		return;

	reverse_list(h1->next, h2);
	add_nodeint_end(h2, h1->n);
}

/**
 * is_palindrome - function checks if list is palindrome
 * @head: head of linked list
 * Return: int 0 if not, 1 if so
 */
int is_palindrome(listint_t **head)
{
	listint_t *h2 = NULL;
	listint_t *for_ward = NULL;
	listint_t *back_ward = NULL;

	if (head == NULL || *head == NULL)
		return (1);

	reverse_list(*head, &h2);

	for_ward = *head;
	back_ward = h2;
	while (for_ward)
	{
		if (for_ward->n != back_ward->n)
		{
			free_listint(h2);
			return (0);
		}
		for_ward = for_ward->next;
		back_ward = back_ward->next;
	}
	free_listint(h2);
	return (1);
}
