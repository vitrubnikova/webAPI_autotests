#!/bin/bash

# Переменные
APP_NAME="myapp"
APP_DIR="/var/www/$APP_NAME"
GIT_REPO="https://github.com/username/myapp.git"
BRANCH="main"
NGINX_CONF="/etc/nginx/sites-available/$APP_NAME"
NGINX_ENABLED="/etc/nginx/sites-enabled/$APP_NAME"

# Остановить выполнение скрипта при ошибке
set -e

# Обновить код из репозитория
echo "Обновление кода из репозитория..."
if [ -d "$APP_DIR" ]; then
  cd "$APP_DIR"
  git fetch origin
  git reset --hard origin/$BRANCH
else
  git clone -b $BRANCH $GIT_REPO $APP_DIR
  cd "$APP_DIR"
fi

# Установить зависимости (если используется npm)
echo "Установка зависимостей..."
npm install

# Собрать проект (если требуется)
echo "Сборка проекта..."
npm run build

# Настройка Nginx
echo "Настройка Nginx..."
sudo tee $NGINX_CONF > /dev/null <<EOL
server {
    listen 80;
    server_name $APP_NAME.com;

    root $APP_DIR/dist;
    index index.html;

    location / {
        try_files \$uri /index.html;
    }

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
EOL

# Создать символическую ссылку, если она еще не существует
if [ ! -f "$NGINX_ENABLED" ]; then
  sudo ln -s $NGINX_CONF $NGINX_ENABLED
fi

# Перезапустить Nginx
echo "Перезапуск Nginx..."
sudo systemctl restart nginx

echo "Деплой завершен успешно!"
