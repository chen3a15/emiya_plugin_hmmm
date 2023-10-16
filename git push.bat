chcp 65001
@echo off
git add .
set /p a="提交描述："
git gc
git commit -m "%a%"
git push
pause