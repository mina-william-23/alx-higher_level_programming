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
	int len_list = 0, len_half;
	listint_t *current = *head;
	int i = 0, j = 0, *arr;

	while (current)
	{
		len_list++;
		current = current->next;
	}
	if (len_list <= 1)
		return (1);

	len_half = len_list / 2;
	arr = malloc(sizeof(int) * len_half);
	current = *head;
	while (current)
	{
		if (i < len_half)
			arr[j++] = current->n;
		else if (i > len_half || (i == len_half && len_list % 2 == 0))
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
