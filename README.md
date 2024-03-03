##  Прокси-сервис для приема сообщений из телеграм-модуля

### Как установать?

Вам понадобится установленный Python 3.11, git, docker-compose

Склонируйте репозиторий или скачайте код в виде архива:
```bash
$ git clone git@github.com:IlyaG96/RestTgProxy.git
```

Создайте в этой папке виртуальное окружение:
```bash
$ python3.11 -m venv [полный путь до папки RestTgProxy] env
```

Активируйте виртуальное окружение и установите все необходимые пакеты:
```bash
$ cd RestTgProxy
$ source env/bin/activate
$ pip install -r requirements.txt
```
### Использование
Задайте переменные окружения любым удобным способом:
```bash
DEBUG=""
HOST=""
PORT=""
INTEGRATION_LOG_ON=""
INTEGRATION_LOG_HOST=""
INTEGRATION_LOG_ENDPOINT=""
INTEGRATION_LOG_PORT=""
```

 -DEBUG - вкл\откл режим отладки - WIP  
 -HOST - хост сервиса
 -PORT - порт основного сервиса  
 -INTEGRATION_LOG_ON - вкл\откл отправку в интеграционный лог  
 -INTEGRATION_LOG_HOST - хост интеграционного лога 
 -INTEGRATION_LOG_ENDPOINT - эндпоинт интеграционного лога 
 -INTEGRATION_LOG_PORT - порт интеграционного лога 

#### Простейший способ запустить бота:
```bash
$ python main.py
```

### Сборка и запуск с использованием Docker

- Соберите контейнер и запустите при помощи docker-compose
```shell
docker-compose up --build
```

Для того, чтобы увидеть список всех работающих образов, введите команду:
```shell
docker images
```
Для того, чтобы увидеть список всех образов, введите команду:
```shell
docker ps
```
Для удаления образа найдите в списке образов id своего образа (IMAGE ID) и выполните команду:
```shell
docker rmi IMAGE_ID   
```