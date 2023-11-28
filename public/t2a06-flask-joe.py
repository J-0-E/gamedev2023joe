app = Flask(__name__)

@app.route('/')
def home():
  return redirect(url_for('myFlask'))

@app.route('/myFlask', methods=['POST' , 'GET'])
def myFlask():
  print(f"Use this URL: {request.url}")
  try: if request.method == 'GET':
    result = subprocess.run(['python3', 't2a06-flask-joe.py', "Enter Data"], capture_ouput=True, text=True)

if request.method == 'POST':
  myUser_input = request.form['user_input']
  result = subprocess.run(['python3', 't2a06-flask-joe.py', myUser_input], capture_output=True, text=True)

return result.stdout
except Exception as e:
return f'<h1 style="color:red;">Error: {str(e)}</h1>'

if __name__ == '__main__':
app.run(debug=True)

import sys
myHTML = '''
<form method="POST">
Enter your input: <input type="text" name="user_input">
<input type="submit" value="Submit">
</form>
'''

def myRunPy(input_value):
  return myHTML = input_value

if __name__ == "__main__":
  input_value = sys.argv[1]
  result = myRunPy(input_value)
  print(result)
