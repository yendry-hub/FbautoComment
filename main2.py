from flask import Flask, request, render_template
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/open_website', methods=['POST'])
def send_messages():
    if request.method == 'POST':
        url = request.form['url']

        driver = Chrome()
        driver.get('https://www.facebook.com/login/')
        time.sleep(4)

        textbox_email = driver.find_element(By.XPATH, '//*[@id="email"]')
        #textbox_email.send_keys(email)
        #textbox_password = driver.find_element_by_xpath('//*[@id="pass"]')
        #textbox_password.send_keys(password)

        #botao = driver.driver.find_element_by_xpath('//*[@id="home"]/div/div/ul/li[2]/div/div/a')
        #botao = driver.find_element_by_xpath('//*[@id="home"]/div/div/ul/li[2]/div/div/a')
        #botao = driver.find_element_by_xpath('//*[@id="home"]/div/div/ul/li[2]/div/div/a')
        botao = driver.find_element(By.XPATH, '//*[@id="home"]/div/div/ul/li[2]/div/div/a')
        botao.click()
        time.sleep(4)
        #driver.get(link)
        #time.sleep(4)

        #texto = driver.find_element_by_xpath(
            #'//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div/div/div/div/form/div[2]/div/div[2]/div')

        #for i in range(qtd_message):
            #texto.send_keys(message, Keys.ENTER)
            #time.sleep(2)

        driver.quit()

        return "Messages sent successfully!"
    else:
        return "Invalid request method"

if __name__ == '__main__':
    app.run(debug=True)
