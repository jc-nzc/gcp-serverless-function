import keen
import random
import time

keen.project_id = ''
keen.write_key = ''
keen.master_key = ''

maps = ['acropolis', 'cyberForest', 'kairosJunction', 'kingsCove', 'newRepug', 'thunderbird']
races = ['terran', 'protoss', 'zerg']
leagues = ['diamond3', 'diamond2', 'diamond1']
results = ['win', 'loss']

def basic_add():
	return(keen.add_event("games", {
		"outcome" : "{0}".format(random.choice(results)),
		"map": "{0}".format(random.choice(maps)),
		"mmr": "{0}".format(random.randint(3700, 4000)),
		"race": "{0}".format(random.choice(races)),
		"league": "{0}".format(random.choice(leagues)),
		"opponent" : {
			"name": "{0}".format(random.choice(['luke', 'leia', 'han', 'chewy', 'benSwolo'])),
			"op_mmr": "{0}".format(random.randint(3600,4100))
			}
		}))


# def delete_event():
	# return(keen.delete_events("games"
		# filters=[{
		# 	"property_name": "keen.id",
		# 	"operator": "eq",
		# 	"property_value": "{0}".format(id)
		# 	}]
		# )
	# )

if __name__ == '__main__':
	for i in range(1,16):
		print(i)
		basic_add()
		time.sleep(60)
