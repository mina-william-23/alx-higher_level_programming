#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if linked list is palindrom
 * @head: linked list
 * Return: 0 if not palindrome 1 is palindrome
 */
int is_palindrome(listint_t **head)
{
	size_t len_list = 0;
	listint_t *current = *head;
	int i = 0, j = 0, *arr;

	while (current)
	{
		len_list++;
		current = current->next;
	}
	if (len_list <= 1)
		return (1);

	arr = malloc(sizeof(int) * ((int)len_list / 2));
	current = *head;
	while (current)
	{
		if (i < (int)len_list / 2)
			arr[j++] = current->n;
		else if (i == (int)len_list / 2 && len_list % 2)
		{
			current = current->next;
			i++;
			continue;
		}
		else
		{
			if (arr[--j] != current->n)
			{
				free(arr);
				return (0);
			}
		}
		i++;
		current = current->next;

	}
	free(arr);
	return (1);
}
