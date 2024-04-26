from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
import time, json
import time
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

database = {}
RunningAll = False
# Function to connect to the database
def connect_db():
    return sqlite3.connect('database.db')

# Function to create the table if it doesn't exist
def create_table():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            comment TEXT
        )
    ''')
    db.commit()
    db.close()

# Route to display the index page with the table of entries
@app.route('/')
def index():
    create_table()
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM entries')
    entries = cursor.fetchall()
    db.close()
    return render_template('index.html', entries=entries)

# Route to handle adding a new entry
@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    phone = request.form['phone']
    password = request.form['password']
    comment = request.form['comment']
    

    db = connect_db()
    cursor = db.cursor()
    try:
         cursor.execute('INSERT INTO entries (name, phone, password, comment) VALUES (?, ?, ?,?)', (name, phone, password, comment))
         db.commit()
         flash('Data added successfully!', 'success')
    except sqlite3.IntegrityError:
            flash('Data already exists!', 'error')
            db.close()

    return redirect(url_for('index'))

# Route to handle editing an entry
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_entry(id):
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        password = request.form['password']
        comment = request.form['comment']
		
        # Update the entry in the database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute('UPDATE entries SET name=?, phone=?, password=?, comment=? WHERE id=?', (name, phone, password, comment, id))
        db.commit()
        db.close()

        return redirect(url_for('index'))

    # Fetch the entry from the database
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM entries WHERE id=?', (id,))
    entry = cursor.fetchone()
    db.close()

    return render_template('edit.html', entry=entry)

# Route to handle deleting an entry
@app.route('/delete/<int:id>')
def delete_entry(id):
    # Delete the entry from the database
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM entries WHERE id=?', (id,))
    db.commit()
    db.close()

    return redirect(url_for('index'))


@app.route('/open_website', methods=['POST'])
def open_website():
    #global RunningAll
    #global url
    #for _ in range(5):
        #response_data = {"status": "nextId"}
        #return jsonify(response_data)
        #time.sleep(5)
    refresh_limit = 10000
    if request.method == 'POST':
        url = request.form['url']
        id = request.form['id']
        email = request.form['phone']
        password = request.form['password']
        comment = request.form['comment']

        driver = Chrome()
        driver.refresh
        try:
            driver.get('https://www.facebook.com/login/')
            time.sleep(1)

            textbox_email = driver.find_element(By.XPATH, '//*[@id="email"]')
            textbox_email.send_keys(email)
            textbox_password = driver.find_element(By.XPATH, '//*[@id="pass"]')
            textbox_password.send_keys(password)
            botao = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
            botao.click()
            time.sleep(2)

            for i in range(1, refresh_limit + 1):
                print(i)
                driver.get(url)
                time.sleep(2)
                
                try:
                    #wait = WebDriverWait(driver, 1)  # 1 seconds timeout
                    #elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), '1 m')]")))    
                    elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '1 m')]")
                    print("Checking 1m")
                    if elements:
                        for element in elements:
                            element.click()
                            print("Posting baru diklik")
                            #RunningAll = True
                            time.sleep(2)

                            elementc = ""
                            elementc = driver.find_elements(By.XPATH, f"//*[contains(text(), 'Comment')]")
                            if elementc:
                                for element in elementc:
                                    element.click()
                                    print("Comment diclick")
                                    time.sleep(1)
                                
                                    textarea_elements = driver.find_elements(By.TAG_NAME, 'p')
                                    # Check if there are any 'p' elements
                                    if textarea_elements:
                                        last_p_element = textarea_elements[-1]  # Negative indexing, -1 refers to the last element
                                        last_p_element.send_keys(comment, Keys.ENTER)
                                        print("Comment dikirim")
                                        time.sleep(3)
                                        driver.quit()
                                        break
                                    else:
                                        print("There are no 'p' elements on the page")
                                        
                                        
                             
                    #elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'Just now')]")))    
                    elementsb = driver.find_elements(By.XPATH, f"//*[contains(text(), 'Just now')]")
                    print("Checking Just now")
                    if elementsb:
                        for element in elementsb:
                            element.click()
                            print("Posting baru diklik")
                            #RunningAll = True
                            time.sleep(2)
                        
                            elementc = ""
                            elementc = driver.find_elements(By.XPATH, f"//*[contains(text(), 'Comment')]")
                            if elementc:
                                for element in elementc:
                                    element.click()
                                    print("Comment diclick")
                                    time.sleep(1)
                                
                                    textarea_elements = driver.find_elements(By.TAG_NAME, 'p')
                                    # Check if there are any 'p' elements
                                    if textarea_elements:
                                        last_p_element = textarea_elements[-1]  # Negative indexing, -1 refers to the last element
                                        last_p_element.send_keys(comment, Keys.ENTER)
                                        print("Comment dikirim")
                                        time.sleep(3)
                                        driver.quit()
                                        break
                                    else:
                                        print("There are no 'p' elements on the page")
                                        
                except Exception as e:
                    print(f"Error in iteration {i}: {e}")        

                #time.sleep(2)  # Introduce a delay of 10 seconds after breaking out of the loop

        except Exception as e:
            return f'Error opening website: {e}'
        finally:
            driver.quit()
    else:
        # Handle GET request (if any)
        return 'Only POST requests are allowed for this endpoint.'

if __name__ == '__main__':
    app.run(debug=True)
