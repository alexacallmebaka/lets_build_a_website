import flask

#app setup
app = flask.Flask(__name__)

names = []

@app.get('/')
def sign_in():
    return flask.render_template('sign_in.html')

@app.get('/signed-in')
def signed_in():
    return flask.render_template('signed_in.html', names=names)

@app.post('/update-names')
def update_names():

    if len(flask.request.form['name']) > 280:
        flask.abort(403)

    names.append(flask.request.form['name'])

    return flask.redirect(flask.url_for('signed_in'))

if __name__ == '__main__':
    sign_in()
