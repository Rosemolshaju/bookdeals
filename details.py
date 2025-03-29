from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_details():
    # Get user details from the form
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    # Email content
    recipient_email = "admin@example.com"  # Replace with the recipient's email
    subject = "User Details Submission"
    body = f"""
    Hello Admin,

    The following details were submitted by a user:
    Name: {name}
    Email: {email}
    Phone: {phone}

    Best regards,
    Your Application
    """

    # Send the email
    try:
        sender_email = "impulesSharjah@gmail.com"  # Replace with sender's email
        password = "Worstisthebest123"              # Use a secure method for storing passwords
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        
        return "Details submitted successfully and email sent!"
    except Exception as e:
        return f"Failed to send email: {e}"

if __name__ == '__main__':
    app.run(debug=True)
