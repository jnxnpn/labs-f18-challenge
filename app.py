from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/pokemon/<query>', methods=['GET'])
def main(query):
	r = requests.get('https://pokeapi.co/api/v2/pokemon/'+query+'/')
	js = r.json()
	##query = query +''
	if query.isdigit():
		st = "the pokemon with number "+ query+" has name " + js["name"]
	else:
		st = "the pokemon with name "+query + " has number " + str(js["id"])
	return st

if __name__ == '__main__':
    app.run()
