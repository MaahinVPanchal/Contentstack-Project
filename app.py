from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

# Contentstack API keys (stored as environment variables for security)
API_KEY = os.getenv('CONTENTSTACK_API_KEY', 'bltc70800559f9ec38f')  # Your Contentstack API Key
DELIVERY_TOKEN = os.getenv('CONTENTSTACK_DELIVERY_TOKEN', 'cs113f5f781661cfbd121dd32f')  # Delivery Token
ENVIRONMENT = os.getenv('CONTENTSTACK_ENVIRONMENT', 'staging')  # Environment ('staging' or 'production')

# Helper function to fetch entries from Contentstack API
def fetch_entries(content_type):
    url = f"https://eu-cdn.contentstack.com/v3/content_types/{content_type}/entries?environment={ENVIRONMENT}"
    headers = {
        "access_token": DELIVERY_TOKEN,
        "api_key": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an exception for HTTP errors
        return response.json().get('entries', [])
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error fetching {content_type}: {e}")
        return []

# Route for the homepage
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title="Home")  # Rendering your homepage

@app.route('/team')
def team():
    team_members = fetch_entries('our_team')  # Fetching team members from Contentstack
    if team_members:
        return render_template('team.html', team_members=team_members, title="Our Team")
    else:
        return render_template('error.html', message="Failed to retrieve team data.", title="Error")


@app.route('/news')
def news():
    headlines = fetch_entries('news')
    if headlines:
        return render_template('news.html', news=headlines, title="News")
    else:
        return render_template('error.html', message="Failed to retrieve news data.", title="Error")

# Route for Categories tab (optional)
@app.route('/categories')
def categories():
    categories = fetch_entries('category')
    if categories:
        return render_template('categories.html', categories=categories, title="Categories")
    else:
        return render_template('error.html', message="Failed to retrieve category data.", title="Error")

# About page
@app.route('/about')
def about():
    about_entry = fetch_entries('about_us_page')  # Assuming 'about_us' is the content type for your about page
    if about_entry:
        about_data = about_entry[0]  # Get the first entry
        return render_template('about.html', about=about_data, title=about_data['title'])
    else:
        return render_template('error.html', message="Failed to retrieve about data.", title="Error")
@app.route('/contact')
def contact():
    contact_info = fetch_entries('contact')  # Assuming 'contact' is the content type for your contact details
    if contact_info:
        contact_data = contact_info[0]  # Get the first entry
        return render_template('contact.html', contact=contact_data, title=contact_data['title'])
    else:
        return render_template('error.html', message="Failed to retrieve contact data.", title="Error")


# Error handler route
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404 - Page Not Found"), 404

if __name__ == "__main__":
    app.run(debug=True)

