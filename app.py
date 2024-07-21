from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the CSV file
df = pd.read_csv('C:/Users/Admin/OneDrive - vit.ac.in/Desktop/SEM 7/Data Mining/Project/House Price India.csv.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    bedrooms = request.form.get('bedrooms')
    bathrooms = request.form.get('bathrooms')
    living_area = request.form.get('living_area')
    
    price_range = request.form.get('price_range')

    # Filter the dataframe based on user input
    filtered_df = df[
        (df['number of bedrooms'] == int(bedrooms)) &
        (df['number of bathrooms'] == float(bathrooms)) &
        (df['living area'].between(*map(int, living_area.split('-')))) &
        
        (df['Price'].between(*map(int, price_range.split('-'))))
    ]

    # Convert the filtered dataframe to a list of dictionaries
    available_houses = filtered_df.to_dict('records')

    return render_template('results.html', houses=available_houses)

if __name__ == '__main__':
    app.run(debug=True)