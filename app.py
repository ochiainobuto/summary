#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
# 追加
from summary import get_summary

# app という名前でFlaskオブジェクトをインスタンス化
app = Flask(__name__)

# rootディレクトリにアクセスした場合の挙動
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        summaries  = get_summary(text)
        return render_template("summary.html", summaries=summaries)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
