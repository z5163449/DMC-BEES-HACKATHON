from main import app
import os
app.secret_key = os.urandom(5)
app.run(debug=True,port=8085)