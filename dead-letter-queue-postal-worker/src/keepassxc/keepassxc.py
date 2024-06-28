from pykeepass import PyKeePass
from properties import Props
import pyotp

# load database
kp = PyKeePass(Props.KEEPASSXC_DBPATH, password=Props.KEEPASSXC_PWD)

# search specific entry
entry = kp.find_entries(title="testentry", first=True)

# get otp
# ootp = entry.otp

# get password
password = entry.password

# get attachments
attachments = entry.attachments

# find specific file, here a certificate
cert = kp.find_attachments(filename='mms-at-work.de.cachain', first=True).data


# get expiry time
expiry_time = entry.expiry_time

# get password
added_attribute = entry.custom_properties.get("added_attribute")

for inp in password, attachments[1].data, expiry_time, added_attribute, cert:
    print(inp)

print(pyotp.parse_uri(entry.otp).now())

# props = __Props()
# print(props.jira_login_token)
