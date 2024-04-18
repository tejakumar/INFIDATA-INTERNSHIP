import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['teja123']).generate()
print(hashed_passwords)