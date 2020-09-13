import keen
import random
import time

keen.project_id = ''
keen.write_key = ''
keen.master_key = ''

campaign_driver = ['email_campaign', 'webinar', 'crm_api_call', 'survey', 'custom_service', 'integration']
cpu = ['Intel', 'AMD', 'Nvidia']
company_uuid = ['101', '102', '103']
results = ['true', 'false']
# v = "{0}".format(random.randint(3600,4100))

def basic_add():
	v = "{0}".format(random.randint(3600,4100))
	return(keen.add_event("campaigns_sent", {
		"order_completed" : "{0}".format(random.choice(results)),
		"campaign_type": "{0}".format(random.choice(campaign_driver)),
		"revenue": "{0}".format(random.randint(3700, 4000)),
		"cpu_type": "{0}".format(random.choice(cpu)),
		"company_id": "{0}".format(random.choice(company_uuid)),
		"completions" : {
			"computer": "{0}".format(random.choice(['macbook', 'surface', 'chromebook', 'xps', 'zenbook'])),
			"opp_rev": int(v)
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
	for i in range(1,100):
		print(i)
		basic_add()
		time.sleep(5)
