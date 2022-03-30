from django.utils.translation import gettext_lazy as _

# contact
CONTACT_QUESTIONS = {
    'contact_title': _('Contact information'),
    'contact_help_text': _('You are not required to provide your name or contact information. If you want to remain anonymous, leave this section blank. If you choose to provide your contact information, we will only use it to respond to your submission.'),
    'contact_name_title': _('Your name'),
    'contact_first_name': _('First name'),
    'contact_last_name': _('Last name'),
    'contact_email': _('Email address'),
    'contact_phone': _('Phone number'),
    'contact_address_line_1': _('Mailing address 1'),
    'contact_address_line_2': _('Mailing address 2'),
    'contact_city': _('City'),
    'contact_zip': _('Zip code'),
    'contact_state': _('State'),
    'referrer': _('Referrer'),
}
SERVICEMEMBER_QUESTION = _('Are you now or have ever been an active duty service member?')

# primary concern
PRIMARY_REASON_QUESTION = _('What is your primary reason for contacting the Civil Rights Division?')
# hate crime
HATE_CRIME_TITLE = _('Primary Issue')
HATE_CRIME_QUESTION = _('Does your situation involve physical harm or threats of violence?')
HATE_CRIME_HELP_TEXT = _('To be considered a hate crime, the physical harm or threats of violence must be based on race, color, national origin, religion, gender, sexual orientation, gender identity, or disability.')

# Location
LOCATION_QUESTIONS = {
    'location_title': _('Where did this happen?'),
    'location_name': _('Organization name'),
    'location_address_line_1': _('Street address 1'),
    'location_address_line_2': _('Street address 2'),
    'location_city_town': _('City/town'),
    'location_state': _('State'),
}
ELECTION_QUESTION = _('What kind of election or voting activity was this related to?')
WORKPLACE_QUESTIONS = {
    'public_or_private_employer': _('Was this a public or private employer?'),
    'employer_size': _('How large is this employer?'),
}
PUBLIC_QUESTION = _('Please choose the type of location that best describes where the incident happened')
POLICE_QUESTIONS = {
    'inside_correctional_facility': _('Did this happen while in custody or incarcerated?'),
    'correctional_facility_type': _('What type of prison or correctional facility?')
}
EDUCATION_QUESTION = _('Did this happen at a public or a private school, educational program or activity?')

# Personal characteristics
PROTECTED_CLASS_QUESTION = _('Do you believe any of these personal characteristics influenced why you were treated this way?')
# Date
DATE_QUESTIONS = {
    'date_title': _('When did this happen?'),
    'last_incident_month': _('Month'),
    'last_incident_day': _('Day'),
    'last_incident_year': _('Year'),
}

# Personal description
SUMMARY_QUESTION = _('In your own words, describe what happened')
SUMMARY_HELPTEXT = {
    'title': _('Please share details like:'),
    'examples': [
        _('Time'),
        _('Names of people involved including witnesses if there are any'),
        _('Any supporting materials (please list and describe them)')],
    'attachments': _('While you <strong>cannot</strong> submit these materials through this site, we may request copies of these from you at a later date. If you provide details of these materials, we can know what will be most helpful for your report.'),
}
