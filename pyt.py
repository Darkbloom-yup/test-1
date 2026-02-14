from flask import Flask, render_template
import os

app = Flask(__name__)

# Все твои маршруты
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/basics')
def basics():
    return render_template('basics.html')

@app.route('/global')
def global_attrs():
    return render_template('global.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/boolean')
def boolean():
    return render_template('boolean.html')

@app.route('/tags')
def tags():
    return render_template('tags.html')

@app.route('/attributes')
def attributes():
    return render_template('attributes.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/examples')
def examples():
    return render_template('examples.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)  # debug=True убран!