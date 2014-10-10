何をするもの？
=============
スクリーンショットをとります 
現在はgbrowseのみ対応しています 

Development Envitonment
=======================
Ubuntu

Prerequisite
============

xvfb 
firefox

python(recommened pyenv, virtualenv)

HOW TO USE
==========
Xvfb :10 -ac 
DISPLAY=:10 python take-screenshot.py position.sample.txt gbrowsesite

position.txtの書式
=================
現在はいかのものに対応しています
+ 遺伝子名
+ 染色体と位置情報

position.txt のサンプル
======================
> chrI,80000,120000
> chrI,110000,114000
> NUT21
> NUT2



SUPPORT SITE
============
gbrowse site

HOW IT WORK
===========
This is using selenium from python
Take screen shot
