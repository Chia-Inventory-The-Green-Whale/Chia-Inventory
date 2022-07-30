import requests

#This would be for collecting Data from spacescan

config = {
    'api_url' : 'https://api2.spacescan.io/api',
    #Please use your own API key
    'api_key' : 'tkn1qqqk2az9qpzedr6lucan4qzf57zs9nmfkptjcfsk2az9qpzevqqq5rzt30'
}

class chianiaCollection:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    

#Which collections we want data from
a_collections = [
    chianiaCollection("Chia Inventory","col16fpva26fhdjp2echs3cr7c30gzl7qe67hu9grtsjcqldz354asjsyzp6wx"),
    chianiaCollection("Chreatures"    ,"col1w0h8kkkh37sfvmhqgd4rac0m0llw4mwl69n53033h94fezjp6jaq4pcd3g")
]


for coll in a_collections:
    response = requests.get(config['api_url'] + '/nft/collection/' + coll.id + "?x-auth-id=" + config['api_key'] + '&coin=xch&page=1&count=40&version=1')
    print(response.json())