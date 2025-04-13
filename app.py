# app.py
from flask import Flask, render_template, url_for, request, redirect, jsonify
import json
import os
from mail import send_mail
app = Flask(__name__)

def load_data(file_path):
    """Load data from a JSON file."""
    with open(file_path) as f:
        return json.load(f)

@app.context_processor
def inject_contact():
    data = load_data('data/data.json')  # Load contact data from data.json
    print("Contact data loaded:", data.get('contact'))  # Debugging statement
    return {'contact': data['contact']}

@app.route('/')
def home():
    data = load_data('data/data.json')  # Load main data for the home page
    projects = load_data('data/projects.json')  # Load projects from projects.json
    return render_template('home.html', data=data, projects=projects)

@app.route('/projects')
def projects():
    projects = load_data('data/projects.json')  # Load projects data
    return render_template('projects.html', projects=projects)

@app.route('/blog')
def blog():
    posts = load_data('data/blog.json')  # Load blog posts data
    return render_template('blog.html', posts=posts)

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/send-message', methods=['POST'])
def send_message():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Compose the email body
    message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    # Use the recipient email from the .env file
    recipient_email = os.getenv('RECIPIENT_EMAIL')  # Email where the message will be delivered
    sender_email = os.getenv('SMTP_USERNAME')  # Email used to send the message

    try:
        # Send the email
        if send_mail(subject, sender_email, recipient_email, message_body):
            return jsonify({"status": "success", "message": "Your message has been sent successfully!"})
        else:
            return jsonify({"status": "error", "message": "Failed to send message. Please try again later."}), 500
    except Exception as e:
        print(f"Failed to send email: {e}")
        return jsonify({"status": "error", "message": "An unexpected error occurred. Please try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)