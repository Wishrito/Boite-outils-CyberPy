import webbrowser

from win11toast import toast

notif = toast("Hello, world!", 'Clic to open URL !',
              buttons=['Approve', 'Dismiss', 'Other'])
redir = ""
match notif.get('arguments'):
    case 'http:Approve':
        redir = 'https://www.python.org/'
    case 'http:Dismiss':
        redir = 'https://www.google.com/'
    case 'http:Other':
        redir = 'https://www.youtube.com/'
webbrowser.open(redir)
