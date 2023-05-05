from flask import Flask, render_template, url_for, request, redirect
import csv
# from markupsafe import escape

app = Flask(__name__)
print(__name__) # __main__

@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/index.html')
# def index():
#     return render_template('index.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')


# Example in Flask documentation, Accessing Request Data, Request object
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

# My solution (working):
# @app.route('/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /
#     return render_template(escape(subpath))

# Andrei solution:
@app.route('/<string:page_name>')
def html_page(page_name):
   return render_template(page_name)

# My solution:
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         write_to_file(data)
#         with open('database.txt', 'a') as f:
#             f.write(str(data))
#         return redirect('/thankyou.html')
#     else:
#         return 'something went wrong. Try again'
#     # return 'form submitted hooorayyy!'

# Andrei solution:
# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')
# 
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         write_to_file(data)
#         return redirect('/thankyou.html')
#     else:
#         return 'something went wrong. Try again'


# def write_to_csv(data):
#     with open('database.csv', mode='a', newline='') as database2:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([email,subject,message])

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         write_to_csv(data)
#         return redirect('/thankyou.html')
#     else:
#         return 'something went wrong. Try again'


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again'


