from flask import Flask, render_template
from selenium import webdriver

app = Flask(__name__)

@app.route('/')
def open_website():
  # Replace with the actual URL you want to open
  url = "https://solusikomputerbekas.com/"

  # **Security Warning:** This is for demonstration only, not production!
  driver = webdriver.Chrome()
  driver.get("https://solusikomputerbekas.com/")

  # Get website title (assuming it's in the title tag)
  title = driver.title

  # Close the browser instance (important)
  #driver.quit()

  return render_template("index.html", title=title)

if __name__ == "__main__":
  app.run(debug=True)
