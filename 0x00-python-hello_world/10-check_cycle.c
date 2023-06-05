#include "lists.h"

/**
 * check_cycle - function checks for loop in LL
 * @list: head of linked list
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *cur, *check;

	if (!list)
	{
		return (0);
	}
	cur = list;
	check = list->next;
	while (check && cur && ckeck->next)
	{
		if (curr == check)
		{
			return (1);
		}
		cur = cur->next;
		check = check->next->next;
	}
	return (0);
}
