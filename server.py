from flask_app.controllers import main
from flask_app import app

if __name__ == "__main__":
  app.run(debug=True)
print("Server connected!")