import csv
# lets us open addresses in the web browser
import webbrowser

cc_email = "danny.kishner@generalassemb.ly"
dannys_phone_number = '1-401-929-9346'

successful_title = 'Congratulations {name}! You were successful!' 
successful_body = '''
Dear {first_name},

Our records show that you have **succeeded**! 
Please let us know if the following information is correct
so that we can send our prize package to the right address!

---

{name}
{company}
{address}

---

Please contact us if the information is incorrect. You can reach us at {dannys_phone_number}.

Sincerely,

> The Record Keepers
'''

failure_title = 'Oh no {name}, it appears that you\'ve lost!'
failure_body = '''
Dear {first_name},

Our records show that you have **failed to succeed** :-(

Please never contact us.

You fail,

> The Record Keepers
'''


def popup_compose(email, title, body, cc_email):
    # this is the query string for gmail compose that yields a pre-set compose window
    link_to_gmail = "https://mail.google.com/mail/?view=cm&fs=1&to={email}&su={title}&body={body}&cc={cc_email}".format(email=email, title=title, body=body,cc_email=cc_email)
    webbrowser.open_new(link_to_gmail)

def load_data(file_name):
    # 'with open' allows opening file without having to do 'file.close'
    with open(file_name, 'r') as f:
        data = csv.reader(f, delimiter=",")
        # list comprehension: https://www.python-course.eu/list_comprehension.php
        data = [row for row in data]
    return data

def main():
    data = load_data('emailer_data.csv')
    headers = []
    for i, row in enumerate(data):
        if i == 0:
            # list comprehension: https://www.python-course.eu/list_comprehension.php
            headers = [h.lower() for h in row]
            continue
        person = {}
        for index, header in enumerate(headers):
            person[header] =  row[index]
        # split indexing
        person['first_name'] = person['name'].split(' ')[0]

        if person['completed'] == '1':
            # passing vars with same name as template string vars is totally fine
            body = successful_body.format(dannys_phone_number=dannys_phone_number, **person)
            title = successful_title.format(**person)

            print "{name} succeeded! sending an email to {email}".format(**person)
            popup_compose(person['email'], title, body, cc_email)
            # collects user input can save it as something if you want. in this case, used to pause between popups
            raw_input("Press Enter to continue...")
            print
        elif person['completed'] == '0':
            body = failure_body.format(**person)
            title = failure_title.format(**person)

            print "{name} failed! sending an email to {email}".format(**person)
            popup_compose(person['email'], title, body, cc_email)
            raw_input("Press Enter to continue...")
            print

# code that runs if the script is run vs imported as a module
if __name__ == '__main__':
    main()