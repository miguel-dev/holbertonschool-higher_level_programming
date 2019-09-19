#include "lists.h"

/**
 * is_palindrome - Checks if a single linked list is palindrome.
 * @head: First element of list.
 *
 * Return: 0 if it's not palidrome and 1 if it's a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int buffer[10000];
	listint_t *h;
	int length;
	int i;
	int j;

	length = 0;
	h = *head;
	while (h->next)
	{
		h = h->next;
		buffer[length] = h->n;
		length++;
	}

	i = 0;
	j = length - 1;
	while (i < j)
	{
		if (buffer[i] != buffer[j])
		{
			return (0);
		}
		i++;
		j--;
	}
	return (1);
}
