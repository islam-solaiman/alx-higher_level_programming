#include "lists.h"
/**
 * insert_node - function inserts node into ordered linked list
 * @head: head of the list
 * @number: integer
 * Return: pointer to the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current_node;

	if (head == NULL)
		return (NULL);

	current_node = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;
	else if ((*head)->n > new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		while (current_node->next && current_node->next->n < new_node->n)
			current_node = current_node->next;
		new_node->next = current_node->next;
		current_node->next = new_node;
	}
	return (new_node);
}
