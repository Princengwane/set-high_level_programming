#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to pointer of head node.
 * @number: Integer number to store in new node.
 * Return: Address of new node, or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node;
listint_t *current;

if (head == NULL)
return (NULL);

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);

new_node->n = number;
new_node->next = NULL;

if (*head == NULL || (*head)->n >= number)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}

current = *head;
while (current->next != NULL && current->next->n < number)
{
current = current->next;
}

new_node->next = current->next;
current->next = new_node;

return (new_node);
}
