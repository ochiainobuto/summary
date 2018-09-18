sudo apt-get -y install git python-pip python-dev python-flask python-wtforms python-arrow python-flask-sqlalchemy python-pymysql python-flaskext.wtf  

sudo pip install --upgrade setuptools  
sudo pip install --upgrade gcloud  
git clone https://github.com/ochiainobuto/summary

cd summary 

sudo install.sh  

sudo systemctl enable summary.service  
sudo systemctl start summary.service  
sudo systemctl status summary.service  
sudo systemctl restart summary.service
