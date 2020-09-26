import random


pics_list = ["https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRx_gxCeLvubZS_AbeLpQNvC_fZBsYrhpsrVg&usqp=CAU",
"https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcROMNgRF6d0l4sqcUULsBUb3sDYz5FDS5l-5A&usqp=CAU",
"https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQJTUJyJKuQbx6gfj8PfmQULUjvHhNOhT8f9Q&usqp=CAU",
"https://www.advancedsciencenews.com/wp-content/uploads/2020/06/graham-holtshausen-fUnfEz3VLv4-unsplash.jpg",
"https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQwAoBAfziaZ3lddPZF6U7eyoV0lfBSW3y05Q&usqp=CAU",
"https://asc-csa.gc.ca/images/astronomie/astronomie-og.jpg",
"https://telescopeobserver.com/wp-content/uploads/2017/08/astronomy-vs-astrology-1024x527.jpeg",
"https://physics.tau.ac.il/sites/exactsci_en.tau.ac.il/files/styles/og_image/public/astrophysics_580X330-15.jpg?itok=ZdMfSPBE",
"https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ_Ie_kNMAkuNniOja3Dm0MPo1qMV93UeE6xQ&usqp=CAU",
"https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQsHZ2QlRLPdKUiq1Bhi_Hz9pXxUTtL58cd5A&usqp=CAU"]


def pic_random(lst):
	index = random.randint(0,9)
	return lst[index]
