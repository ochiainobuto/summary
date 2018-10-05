<GCEでインスタンスを作成＞＞＞debianでよい>

<ネットワークから、静的な内部IPアドレスから、静的アドレスを予約をクリックし、新規のIPを追加>

sudo apt-get -y update

sudo apt-get -y install git python-pip python-dev python-flask python-wtforms python-arrow python-flask-sqlalchemy python-pymysql python-flaskext.wtf  

sudo pip install --upgrade setuptools  
sudo pip install --upgrade gcloud  
git clone https://github.com/ochiainobuto/summary  


sudo pip install numpy  
sudo pip install scipy --no-cache-dir  
sudo pip install gensim --no-cache-dir  
sudo pip install janome --no-cache-dir  

>>>>>>>>>>>>>>>>>>>>>>>>>  
sudo python app.py  
#sudoで執行する場合、ライブラリーもsudoでインストールしなければ読み込めない  
#改行は半角スペースを２つ  
>>>>>>>>>>>>>>>>>>>>>>>>>  

cd summary 

sudo install.sh  

sudo systemctl enable summary.service  
sudo systemctl start summary.service  
sudo systemctl status summary.service  

sudo systemctl stop summary.service

sudo systemctl restart summary.service

<app.pyを新規で作ったら>

chmod 700 /home/nononononobuchan/summary/app.py
