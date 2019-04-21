import main_journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------------')
    print('        Journal App')
    print('-------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = 'empty'
    journal_name = 'default'
    journal_data = main_journal.load(journal_name)

    while cmd != 'X' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[X]it: ').upper().strip()
        if cmd == 'L':
            list_entries(journal_data)

        elif cmd == 'A':
            add_entry(journal_data)

        elif cmd != 'X' and cmd:
            print("Sorry, we don't understand '{}'".format(cmd))

    main_journal.save(journal_name, journal_data)
    print('DEBUG: Ending run_event_loop()')


def list_entries(data):
    print("Your journal entries... ")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print(f"* [{idx+1}]  **{entry}")


def add_entry(data):
    print(f'adding to..{data}')
    text = input('Type your entry, <enter> to exit: ')
    main_journal.add_entry(text, data)


main()
