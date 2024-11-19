from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/map', methods=['POST'])
def map():
    query = request.form['query']
    # load the geopandas VS30 data frame and filter it based on the query
    # make the folium map
    return
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', title='VS30 Map')

if __name__ == '__main__':
    app.run()
