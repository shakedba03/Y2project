import random
facts_dict = {
	1 : ["Space is completely silent.", 
	"There is no atmosphere in space, which means that sound has no medium or way to travel to be heard. Astronauts use radios to stay in communication while in space, since radio waves can still be sent and received."],
	2 : ["The hottest planet in our solar system is 450° C.",
	"Venus is the hottest planet in the solar system and has an average surface temperature of around 450° C. Interestingly, Venus is not the closest planet to the Sun – Mercury is closer but because Mercury has no atmosphere to regulate temperature it has a very large temperature fluctuation."],
	3 : ["There may be life on Mars.",
	"Of all the planets in our solar system (apart from Earth), Mars is the one most likely to be hospitable to life. In 1986, NASA found what they thought may be fossils of microscopic living things in a rock recovered from Mars."],

	4: ["Nobody knows how many stars are in space.",
	"The sheer size of space makes it impossible to accurately predict just how many stars we have. Right now, scientists and astronomers use the number of stars only within our galaxy, The Milky Way, to estimate. That number is between 200-400 billion stars and there are estimated to be billions of galaxies so the stars in space really are completely uncountable."],

	5: ["Halleys Comet won’t orbit past Earth again until 2061.",
	"Discovered in 1705 by Edmond Halley, the famous comet was last seen in 1986 and is only seen once every 75 to 76 years."],

	6: ["A full NASA space suit costs $12,000,000.",
	"While the entire suit costs a cool $12m, 70 percent of that cost is for the backpack and control module."],

	7: ["Neutron stars can spin 600 times per second.",
	"Neutron stars are the densest and tiniest stars in the known universe and although they only have a radius of about 10 km (6 mi), they may have a mass of a few times that of the Sun. They can rotate at up to 60 times per second after they are born from a core-collapse supernova star explosion and have been known to spin as fast as 600-712 times per second because of their physics."],

	8: ["There may be a planet made out of diamonds.",
	"As space facts go, this is pretty impressive. Research by Yale University scientists suggests that a rocky planet called 55 Cancri e — which has a radius twice Earth’s, and a mass eight times greater – may have a surface made up of graphite and diamond. It’s 40 light years away but visible to the naked eye in the constellation of Cancer."],

	9: ["The footprints on the Moon will be there for 100 million years.",
	"The Moon has no atmosphere, which means there is no wind to erode the surface and no water to wash the footprints away. This means the footprints of the Apollo astronauts, along with spacecraft prints, rover-prints and discarded material, will be there for millions of years."],

	10: ["One day on Venus is longer than one year.",
	"Venus has a slow axis rotation which takes 243 Earth days to complete its day. The orbit of Venus around the Sun is 225 Earth days, making a year on Venus 18 days less than a day on Venus."],

	11: ["In 3.75 billion years the Milky Way and Andromeda galaxies will collide.",
	"The Andromeda Galaxy is approaching the Milky Way – where our solar system is – at rate of around 110 kilometres per second (68 mi/s) and eventually the two will collide to form a giant elliptical galaxy."],

	12: ["If two pieces of the same type of metal touch in space they will permanently bond.",
	"This incredible fact is also known as cold welding and it happens because the atoms of two pieces of metal have no way of knowing they are separate. This doesn’t happen on Earth because of the air and water found between the pieces."],

	13: ["There is floating water in space.",
	"Astronomers have found a massive water vapor cloud which holds 140 trillion times the mass of water in the Earth’s oceans somewhere around 10 billion light years away – making it the largest discovery of water ever found."],

	14: ["The largest known asteroid is 965 km (600 mi) wide.",
	"Discovered by Italian astronomer Giuseppe Piazzi in 1801, the dwarf planet Ceres was the first, and largest, object to be considered an asteroid. It is located in the Asteroid Belt between the orbits of Mars and Jupiter and accounts for 33% of the entire belt’s mass."],

	15: ["The Moon was once a piece of the Earth.",
	"The theory is that when Earth was a relatively young planet, it was struck by a giant object and this collision broke a piece of the Earth away to create the moon. This piece then began to orbit the Earth as a result of its gravitational pull."],

	16: ["The Sun’s mass takes up 99.86 percent of the solar system.",
	"Made of three quarters hydrogen and helium for most of its remaining mass, the Sun accounts for 99.86 percent of the mass in our solar system with a mass of around 330,000 times that of Earth."],

	17: ["There is a volcano on Mars three times the size of Everest.",
	"At 600 km wide and 21 km high, Olympus Mons is a volcano on Mars that may still be active, according to scientists. It is the tallest peak of any planet. However, the Rheasilvia central peak on the asteroid Vesta is taller at 22 km."],

	18: ["Stars and sand.",
	"There are more stars in the universe than grains of sand on all the beaches on Earth. That’s at least a billion trillion!"],

	19: ["The Apollo astronauts' footprints on the moon will probably stay there for at least 100 million years",
	"Since the moon doesn't have an atmosphere, there's no wind or water to erode or wash away the Apollo astronauts' mark on the moon. That means their footprints, roverprints, spaceship prints, and discarded materials will stay preserved on the moon for a very long time."],

	20: ["99 percent of our solar system's mass is the sun",
	"Our star, the sun, is so dense that it accounts for a whopping 99 percent of the mass of our entire solar system. That's what allows it to dominate all of the planets gravitationally."]

}

def choose_random_facts(dict):
	chosen_keys = []
	while len(chosen_keys) != 5:
		key = random.randint(1,20)
		if key not in chosen_keys:
			chosen_keys.append(key)
	return chosen_keys


	