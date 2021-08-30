from flask import Flask,render_template, url_for, request, redirect
import csv
super = Flask(__name__)

@super.route("/")
def my_home():
    return render_template('index.html')

@super.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('./templates/databas.txt', mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(database2, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@super.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method== 'POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect('./thankyou.html')
    else:
        return 'Something went wrong. Try again!'

if __name__=='__main__':
    super.run(debug=True)