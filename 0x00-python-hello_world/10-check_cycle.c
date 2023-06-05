#include "lists.h"

/**
 * check_cycle - function checks for loop in LL
 * @list: head of linked list
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *current, checker;

	if (!list)
	{
		return (0);
	}
	current = list;
	checker = list->next;
	while (checker && current && checker->next)
	{
		if (current == checker)
		{
			return (1);
		}
		current = current->next;
		chcker = checker->next->next;
	}
	return (0);
}
