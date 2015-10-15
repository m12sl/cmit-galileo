# CMIT Galileo Guide
## Подготовка

Загрузить файлы на плату:
```
scp -r ./ root@galileo:/home/root
```
`galileo` здесь и далее -- адрес платы в локальной сети.

Установить недостающие python пакеты:
```
pip install -r requirements.txt
```

Проверить, что все работает. Для этого нужно запустить на плате в разных терминалах   
```
# terminal
cd /home/root
python web.py

# Another one
cd /home/root
python worker.py
```

Затем слать запросы с компа:

```
curl -X POST galileo:5000/led/on
curl -X POST galileo:5000/led/off
```

Если все нормально, можно запускать наши скрипты как сервисы

## Запуск сервисов

1. Правим `systemd-configs`, проверяем пути, они должны быть абсолютными и для интерпретатора и для файлов

2. Загружаем файлы в `/lib/systemd/system`
  ```
  cp ~/systemd-configs/* /lib/systemd/system/
  ```
  _в предположении, что мы залили всю папку проекта на плату_
  Обратите внимание на пути, а именно `systemd` и `system`. Имеет смысл разобраться в схеме директорий.
  
3. Создаем симлинки `/etc/systemd/system`
  ```
  ln -s /lib/systemd/system/cmit-web.service /etc/systemd/system/cmit-web.service
  ln -s /lib/systemd/system/cmit-worker.service /etc/systemd/system/cmit-worker.service
  ```
  Обратите внимание, пути абсолютные
  
4. Перезагружаем список сервисов и добавляем наши
  ```
  systemctl daemon-reload
  systemctl enable cmit-web.service
  ```
  Последнюю операцию повторить и для `worker`-сервиса.
  
5. Запускаем сервисы
  ```
  systemctl start cmit-web.service
  ```
  Аналогично для `worker`.
  
6. С сервисами можно делать что нужно
  ```
  systemctl status xxx.service
  systemctl stop xxx.service
  systemctl start xxx.service
  systemctl disable xxx.service
  ```
