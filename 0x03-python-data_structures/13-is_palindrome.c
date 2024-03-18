#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (0);

	size_t len = list_len(*head);
	char *str1, *str2;
	size_t mid = len / 2, i;
	int odd = len % 2;

	if (len == 0)
		return (1);
	if (odd)
		len--;
	str1 = malloc(sizeof(char) * mid + 1);
	str2 = malloc(sizeof(char) * mid + 1);

	for (i = 0; i < len; i++)
	{
		if (i < mid)
			str1[i] = (*head)->n;
		else
		{
			if (odd && i == mid)
				*head = (*head)->next;
			str2[i - mid] = (*head)->n;
		}
		*head = (*head)->next;
	}
	rev_string(str2);
	if (strcmp(str1, str2) == 0)
	{
		free(str1);
		free(str2);
		return (1);
	}
	else
	{
		free(str1);
		free(str2);
		return (0);
	}
}

/**
 * list_len - returns number of elements in linked list
 * @h: pointer to head of list
 *
 * Return: length of list
 */
size_t list_len(const listint_t *h)
{
	size_t h_len = 0;

	while (h != NULL)
	{
		h_len++;
		h = h->next;
	}
	return (h_len);
}

/**
* rev_string -  reverses a string
* @s: pointer
* Return: void
*/
void rev_string(char *s)
{
	int i = 0, len = 0;
	char temp;

	while (s[len] != '\0')
		len++;
	len--;

	while (i <= len)
	{
		temp = s[i];
		s[i] = s[len];
		s[len] = temp;
		i++;
		len--;
	}
}
