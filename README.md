><GCEでインスタンスを作成＞＞＞debianでよい>>>>HTTPトラフィックを許可するにチェック>　　

><ネットワークから、静的な内部IPアドレスから、静的アドレスを予約をクリックし、新規のIPを追加>　　

>※プロジェクトでサービスアカウントを作ってない場合　　
>APIとサービスから、認証情報へ。認証情報を作成で、サービスアカウントを選択。新しいサービスアカウントを選択しサービスアカウント名を入力 　　
   
><VMインスタンスを停止し、VMインスタンスの詳細から編集し、サービス アカウントを作ったものに変更>　　

sudo apt-get -y update

sudo apt-get -y install git python-pip python-dev python-flask python-wtforms python-arrow python-flask-sqlalchemy python-pymysql python-flaskext.wtf  

sudo pip install --upgrade setuptools  
sudo pip install --upgrade gcloud  

git clone https://github.com/ochiainobuto/summary  
>※ZIPで上げるなら  
>sudo apt-get install unzip  
>unzip xxxx.zip  

sudo pip install numpy  
sudo pip install scipy --no-cache-dir  
sudo pip install gensim --no-cache-dir  
sudo pip install janome --no-cache-dir  

sudo pip install pydub --no-cache-dir  
sudo pip install --upgrade google-api-python-client
sudo pip install google-cloud-speech

>>>>>>>>>>>>>>>>>>>>>>>>>  
sudo python app.py  
>#sudoで実行する場合、ライブラリーもsudoでインストールしなければ読み込めない  
>#.serviceで起動しないと、SSHを閉じるとアクセスできない。  
>#githubの改行は半角スペースを２つ  
>>>>>>>>>>>>>>>>>>>>>>>>>  

cd summary 

sudo sh install.sh  

sudo systemctl enable summary.service  
sudo systemctl start summary.service  
sudo systemctl status summary.service  

sudo systemctl stop summary.service  
sudo systemctl restart summary.service  

<app.pyを新規で作ったら>  
chmod 700 /home/nononononobuchan/summary/app.py  

<.shが実行できないとき、shをつけて実行>  
sh test.sh  

<status summary.serviceでエラーが出るとは>  
$ less /var/log/syslog  
これでログから原因究明（lessを閉じるときは"q"をタイプ）  
http://takeg.hatenadiary.jp/entry/2017/02/14/233109   

Oct  5 06:31:43 instance-7 app.py[12146]: /usr/bin/env: ‘python\r’: No such file or directory  
そんなファイルがないといわれると、app.pyの改行コードが間違ってる場合も！  

「このエラーに含まれている「\r」 というのは CR ですね。  
改行コードを CR+LF にした覚えはないのですが、改行コードを LF だけにしたら動作するようになりました。 
vi でやる場合にはファイルを開いて以下のコマンドを打ってから、ファイルを保存してやれば OK です。」  
https://blog.cles.jp/item/10164  

vi app.py（app.pyを修正、コマンドで:set ff=unixを叩いてから保存）  
:set ff=unix  
:wq  
http://takeg.hatenadiary.jp/entry/2017/02/14/233109    

<.serviceで起動したときは、import python内の参照ファイルはフルパスで指定する>  
/home/nononononobuchan/summar/wiki.model  

<viを保存せずに終了は？>  
:q!  

<Flakの同時アクセスを処理できるようにする設定方法>  
app.run(host='localhost', port=3000, threaded=True)  


