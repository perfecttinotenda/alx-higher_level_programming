#include "lists.h"


/**
 * check_cycle - ma fankshen ano tarisa
 * @list: kutanga kwema poyinda ema nod
 * Return: 0 kana pasina risakol, 1 kana iripo
 */

int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	check = current->next;

	while (current != NULL && check->next != NULL
			&& check->next->next != NULL)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
