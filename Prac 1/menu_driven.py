name = input('Enter name: ').capitalize()
print('(h)Hello\n(g)Goodbye\n(q)Quit')
menu_choice = input('Please choose from the menu options: ').upper()
while menu_choice != 'Q':
    if menu_choice == 'H':
        print('Hello', name, )
    elif menu_choice == 'G':
        print('Goodbye', name)
    else:
        print('Invalid input.')
    print('(h)Hello\n(g)goodbye\n(q)quit')
    menu_choice = input('Please choose from the menu options: ').upper()
print('finished')
