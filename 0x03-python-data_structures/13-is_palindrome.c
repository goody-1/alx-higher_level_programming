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
	size_t len = list_len(*head);
	int *arr1, *arr2, odd = len % 2;
	size_t mid = len / 2, i, j, loop_len;

	if (len == 0 || *head == NULL)
		return (1);
	arr1 = malloc(sizeof(int) * mid + 1);
	arr2 = malloc(sizeof(int) * mid + 1);

	if (arr1 == NULL || arr2 == NULL)
		return (0);

	loop_len = odd ? len - 1 : len;
	for (i = 0; i < loop_len; i++)
	{
		if (i < mid)
			arr1[i] = (*head)->n;
		else
		{
			if (odd && i == mid)
				*head = (*head)->next;
			j = i - mid;
			arr2[j] = (*head)->n;
		}
		*head = (*head)->next;
	}

	rev_array(arr2, mid - 1);
	if (compare_arrays(arr1, arr2, mid) == 1)
	{
		free(arr1);
		free(arr2);
		return (1);
	}
	else
	{
		free(arr1);
		free(arr2);
		return (0);
	}
}

/**
 * compare_arrays - compares two arrays
 *
 * @arr1: pointer to first array
 * @arr2: pointer to second array
 * @len: length of arrays
 *
 * Return: 1 if arrays are equal, 0 otherwise
*/
int compare_arrays(int *arr1, int *arr2, size_t len)
{
	size_t i;

	for (i = 0; i < len; i++)
	{
		if (arr1[i] != arr2[i])
			return (0);
	}
	return (1);
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
* rev_array -  reverses an array of integers
* @arr: pointer
* @len: length of array
* Return: void
*/
void rev_array(int *arr, int len)
{
	int i = 0, temp;

	while (i < len)
	{
		temp = arr[i];
		arr[i] = arr[len];
		arr[len] = temp;
		i++;
		len--;
	}
}
