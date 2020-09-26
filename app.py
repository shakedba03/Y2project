from flask import *
from flask_mail import *
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
	#print(card_1 + "******************************")
	return render_template("index.html", pic_date = pic_date, pic_explanation = pic_explanation, pic_url = pic_url,
		card_1 = card_1, card_2 = card_2, card_3= card_3, card_4= card_4, card_5 = card_5)

@app.route('/blog', methods=['GET', 'POST'])
def blog_page():
	if request.method == 'POST':
		name = request.form['name']
		title = request.form['title']
		text = request.form['text']
		day = time.strftime("%d")
		month = time.strftime("%b")
		picture = pic_random(pics_list)
		print(title, picture, name, text, day, month)
		add_blog(title, picture, name, text, day, month)
		 
	return render_template("blog.html", blogs=return_all_blogs())

@app.route('/single_blog/<int:blog_id>')
def single_blog_page(blog_id):
	return render_template("single-blog.html", blog = return_blog(blog_id))




if __name__ == '__main__':
    app.run(debug=True)