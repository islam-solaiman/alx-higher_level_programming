#include "lists.h"

/**
 * check_cycle - function checks for loop in LL
 * @list: head of linked list
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *list)
{
	int id;
	int i;
	listint_t *current = NULL;
	listint_t *checker = NULL;

	x = 0;
	current = list;
	while (current)
	{
		i = 0;
		checker = list;
		while (i < id)
		{
			if (checker == current)
				return (1);
			i++;
			checker = checker->next;
		}
		x++;
		current = current->next;
	}
	return (0);
}
