from flask_wtf import Form, RecaptchaField
from wtforms import StringField, TextAreaField, RadioField
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import DataRequired


class SignUpForm(Form):
    org_name = StringField("Organization name", validators=[DataRequired("You need to specify the name of your organization.")])

    website_url = URLField("Website URL", validators=[DataRequired("You need to specify website of the organization.")])
    logo_url = URLField("Logo image URL")
    api_url = URLField("API URL")

    description = TextAreaField("How are you using our API?", validators=[DataRequired("Please, tell us how you (will) use our API.")])

    address_street = StringField("Street")
    address_city = StringField("City")
    address_state = StringField("State")
    address_postcode = StringField("Postcode")
    address_country = StringField("Country")

    contact_name = StringField("Contact name", validators=[DataRequired("You need to provide name of the person to contact.")])
    contact_email = EmailField("Contact email", validators=[DataRequired("Email of contact person is required.")])

    payment_method = RadioField(
        "Choose a payment method:",
        choices=[
            ("paypal", "PayPal"),
            ("stripe", "Stripe"),
            ("invoicing", "Invoicing"),
            ("bitcoin", "Bitcoin"),
        ],
        validators=[DataRequired(message="You need to choose a payment method!")])

    recaptcha = RecaptchaField()
