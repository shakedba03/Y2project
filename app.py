from flask import *
#from flask_mail import *
from databases import *
from flask import session as login_session
from facts import *
from pics import *
import requests
import json
import datetime


app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
time= datetime.datetime.now()


is_signed = False

@app.route('/')
def home_page():
	#Uses NASA's API:
	response = requests.get("https://api.nasa.gov/planetary/apod?api_key=P0sKdiotXiFwGX8J4N3rWli9RFt63IymOHvJF0xT")
	str_j = json.dumps(response.json())
	obj = json.loads(str_j)
	pic_date = obj["date"]
	pic_explanation = obj["explanation"]
	pic_url = obj["hdurl"]
	#Random Facts:
	keys_list = choose_random_facts(facts_dict)
	card_1 = facts_dict[keys_list[0]]
	card_2 = facts_dict[keys_list[1]]
	card_3 = facts_dict[keys_list[2]]
	card_4 = facts_dict[keys_list[3]]
	card_5 = facts_dict[keys_list[4]]
	
	return render_template("index.html", pic_date = pic_date, pic_explanation = pic_explanation, pic_url = pic_url,
		card_1 = card_1, card_2 = card_2, card_3= card_3, card_4= card_4, card_5 = card_5)

@app.route('/blog', methods=['GET', 'POST'])
def blog_page():
	global is_signed
	msg = "- Please log in first."
	if "username" in login_session:
		msg = " "

	if request.method == 'POST' and "username" in login_session:
		name = request.form['name']
		title = request.form['title']
		text = request.form['text']
		day = time.strftime("%d")
		month = time.strftime("%b")
		picture = pic_random(pics_list)
			
		add_blog(title, picture, name, text, day, month)
		 
	return render_template("blog.html", blogs=return_all_blogs(), msg = msg)

@app.route('/single_blog/<int:blog_id>')
def single_blog_page(blog_id):
	return render_template("single-blog.html", blog = return_blog(blog_id))

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
	username_check = "Sign Up"
	if request.method == 'POST':
		username = request.form["username"]
		password = request.form["password"] 
		user = return_user(username)
		if user != None:
			if username == user.username:
				username_check = "Sorry, this username is already taken!"
				return render_template("signup.html", username_check = username_check)	
		add_user(username, password)
		#return redirect(url_for('login_page'))
	return render_template("signup.html", username_check = username_check)



@app.route('/login', methods=['GET', 'POST'])
def login_page():
	global is_signed
	user_check = "Log In"
	pass_check = "Password"
	username_found = False
	pass_found = False
	if request.method == 'POST':
		username = request.form["username"]
		password = request.form["password"]
		users_list = return_all_users()

		for user in users_list:
			if user.username == username and user.password == password:
				is_signed  = True
				username_found = True
				pass_found = True
				login_session["username"] = username
				return redirect(url_for('blog_page'))
			elif user.username == username and user.password != password:
				username_found = True

			elif user.username != username and user.password == password:
				pass_found = True

		if username_found and not pass_found:
			pass_check = "Sorry, this password is incorrect."
			return render_template("login.html", username = user_check, password = pass_check)

		elif not username_found and pass_found:
			user_check = "Sorry, this username is incorrect."
			return render_template("login.html", username = user_check, password = pass_check)

		elif not username_found and not pass_found:
			user_check = "Sorry, this username is incorrect."
			pass_check = "Sorry, this password is incorrect."
			return render_template("login.html", username = user_check, password = pass_check)

	return render_template("login.html", username = user_check, password = pass_check)
	return render_template("login.html")


@app.route('/about')
def about_page():
	return render_template("about.html")



if __name__ == '__main__':
    app.run(debug=True)