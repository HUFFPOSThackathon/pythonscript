############################# API FOR HuffPost Chatbot ##############################
from bot.models import person
def mapLatitudeToPincode(lattitude,longitude):
	################# give constituency info based on latitude and longitude #######
	pass
def getConstituency(pincode=None,latitude=None,longitude=None):
	########## get constituency name from  pincode given it is not null else call constituency mapping function and save it in the current user's database ########
	pass

def registerUserLocation(fbid,pincode=None,latitude=None,longitude=None):
	########### register the user location by getConstituency #######
	pass

def constituencyInfo(fbid):
	################ Gives Manifesto link,MlA name according to location in Fbid############
	current_person=person.objects.filter(fbid=fbid)[0]
	if (current_person.location=="noida"):
		return {"Mla Name":"Pankaj Singh","Manifesto link":"http://timesofindia.indiatimes.com/elections/assembly-elections/uttar-pradesh/news/bjp-releases-poll-manifesto-for-uttar-pradesh-highlights/listshow/56831761.cms"}
	if (current_person.location=="mainpuri"):
		return {"Mla Name":"Raju Yadav","Manifesto link":"http://timesofindia.indiatimes.com/elections/assembly-elections/uttar-pradesh/interactives/samajwadi-partys-manifesto-for-up-polls-highlights/articleshow/56715454.cms"}
	if (current_person.location=="karhal"):
		return {"Mla Name":"Sobaran Singh","Manifesto link":"http://timesofindia.indiatimes.com/elections/assembly-elections/uttar-pradesh/interactives/samajwadi-partys-manifesto-for-up-polls-highlights/articleshow/56715454.cms"}
	
def registerIssue(fbid,Issue):
	######### Register Issue at your OWN location by getting name from calling getConstituency funtion to get  and Trigger on database to check whether the issue has been repoted many times#############
	pass
def getMLADetails(fbid):
	######## FROM  fbid queryuser location and give mla suitably ##########
	current_person=person.objects.filter(fbid=fbid)[0]
	if current_person.location=="noida":
		return "Name Of Mla:Pankaj Singh \n Contact Detail:9868074022"

	else:
		if current_person.location=="mainpuri":
			return "Name Of Mla:Raju Yadav \n Contact Detail:9560117494"

		else:
			return "Name of Mla:Sobaran Singh Yadav \n Contact Detail:8800125071"





def genElectionSummary(electionName):
	####################  get the election name at select the csv you want to query for ad return the tota #########
	pass