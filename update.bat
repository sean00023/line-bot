echo update current file to github
git add .
git commit -am "update time: %date% %time%"
git push -u origin master
pause