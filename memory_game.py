#!/usr/bin/env python

import click
from random import randint
from time import sleep

def generate_elements(num_elements):
	return [randint(0,9) for x in range(num_elements)]

def print_elements_in_row_and_wait(elements_to_print, wait_time):
	for x in elements_to_print:
		print("{} ".format(x), end='', flush=True)
	sleep(wait_time)

def count_user_correct_guesses(memory_items):
	count_correct = 0
	user_guess = click.prompt('Enter as many elements as you can recall')

	while len(user_guess) > 0:
		try:
			next_int = int(user_guess[0])
			user_guess = user_guess[1:]
			if next_int == memory_items[0]:
				count_correct += 1
				print("You got {} right!".format(next_int))
				memory_items = memory_items[1:]
		except ValueError:
			user_guess = user_guess[1:]

	return count_correct


@click.command()
@click.option('--elements', default=5, prompt='how many numbers?')
@click.option('--wait_time', default=10, prompt='wait time for memorization?')
def memory_game(elements, wait_time):
	memory_items = generate_elements(elements)
	print_elements_in_row_and_wait(memory_items, wait_time)

	click.clear()
	count_correct = count_user_correct_guesses(memory_items)
	print("You got {} of the numbers!".format(count_correct))

if __name__ == '__main__':
	memory_game()