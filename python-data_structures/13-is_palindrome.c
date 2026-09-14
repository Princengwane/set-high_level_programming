#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of head node
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head;
listint_t *prev = NULL, *next = NULL, *curr = NULL;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
slow = slow->next;
}

curr = slow;
while (curr != NULL)
{
next = curr->next;
curr->next = prev;
prev = curr;
curr = next;
}

slow = *head;
fast = prev;
while (fast != NULL)
{
if (slow->n != fast->n)
return (0);
slow = slow->next;
fast = fast->next;
}

return (1);
}
