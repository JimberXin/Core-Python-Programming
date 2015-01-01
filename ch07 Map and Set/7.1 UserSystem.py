"""
  Author: Junbo Xin
  Date:  2014/12/25
  Function:
    A very simple user login system. In the main function, display the menu
  for the users.
    1)  If the choice is  'N', then input the new user name. If the name has existed, then
    try again until it's not yet existed. Otherwise save it in the db dictionary.
    2)  If the choice is 'E', then input the old user name and the password.
    3)  Exist.
"""


db = {}


# new user system, for new user to register
def new_user():
    prompt = 'Create a new user name: '
    while True:
        name = raw_input(prompt)
        if name in db:
            prompt = 'Name has already existed, try another'
            continue
        else:
            break
    while True:
        password = raw_input('password: ')
        password2 = raw_input('Confirm your password:')
        if password == password2:
            db[name] = password
            break
        else:
            print 'different passwords in two times, please reset password!'
            continue


# old user system, for old user to login
def old_user():
    name = raw_input('User Login: ')
    pwd = raw_input('password: ')
    password = db.get(name)
    if password == pwd:
        print 'Welcome back! ', name
    else:
        print 'wrong user or password!'


def show_menu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
Enter choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou Pick: [%s]' % choice
            if choice not in 'neq':
                print 'Invalid option, please try again: '
            else:
                chosen = True

        if choice == 'q':
            done = True
        elif choice == 'n':
            new_user()
        elif choice == 'e':
            old_user()


if __name__ == '__main__':
    show_menu()

