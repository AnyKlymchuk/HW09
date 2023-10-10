def check_answer():

    answer = input('The total number of bytes used: ')
    if answer != '500516':
        print('Incorrect')

    answer = input('The average number of bytes per request: ')
    if answer != '500.516' or answer != '500,516':
        print('Incorrect')

    answer = input('The most popular country: ')
    if answer != 'India':
        print('Incorrect')

    answer = input('The user who is on the 3rd place by the number of bytes: ')
    if answer != 'fjfyqotm':
        print('Incorrect')

    answer = input('The number of bytes used by users from Ukraine: ')
    if answer != '51535':
        print('Incorrect')

    answer = input('The number of unique users: ')
    if answer != '500':
        print('Incorrect')

    answer = input('The difference between the average number of bytes per request between users \
from Ukraine and the UK: ')
    if answer != '-33':
        print('Incorrect')
    if answer != '33':
        print('Check sign before number')

    answer = input('The average number of bytes per IP address: ')
    if answer != '1001':
        print('Incorrect')

    answer = input('The total number of users from Europe: ')
    if answer != '242':
        print('Incorrect')