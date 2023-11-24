cd ../
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo apt-get install alien
sudo alien google-chrome-stable_current_x86_64.rpmsudo apt-get install alien
dpkg -i google-chrome-stable_119.0.6045.159-2_amd64.deb
google-chrome-stable --version
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.159/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
chmod 777 chromedriver-linux64/chromedriver
sudo cp -r chromedriver-linux64/chromedriver magical_spider/config/chromedriver
pip install git+https://www.github.com/ultrafunkamsterdam/undetected-chromedriver@master
pip install flask
#pip install sqlite3
pip install selenium
pip install websockets
pip install opencv-python
pip install numpy