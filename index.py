from flask import Flask, Response
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    temp = None
    text_ = ("Jeder freche Junge ist in der Garage. Jede junge Frau läuft ins Geschäft. Junges Ding schläft.")

    if request.method == 'POST' and 'name' in request.form:
        name = request.form['name']
        temp = name
        # doc = nlp(name)
        # name = check_for_adjectives(doc)
    return render_template('index.html', name=name, temp=temp)

if __name__ == '__main__':
    app.run(debug=True)
