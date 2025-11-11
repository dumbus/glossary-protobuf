## RPC. gRPC. Protobuf (Отчёт)

> Дисциплина "Проектирование и развертывание веб-решений в эко-системе Python"

### Шаги работы

1. Реализуйте задание практики, опубликованное по ссылке, с использованием gRPC, protobuf, предоставьте ссылку на репозиторий GitHub со всеми необходимыми компонентами для развертывания.
2. В репозитории отразите отчет с помощью файла с разметкой Markdown, где демонстрировался бы процесс развертывания и работы сервиса.

### Описание выполнения работы

1. Разработка rest-api приложения

<img width="1916" height="748" alt="1" src="https://github.com/user-attachments/assets/31e450b6-c124-4d2e-a52e-9c7b1f6f6621" />

2. Структура файлов разработанного приложения

<img width="296" height="347" alt="2" src="https://github.com/user-attachments/assets/40f8757e-67c6-4ce2-9bb1-ddc18ca7c28c" />  

3. Инструкция по запуску приложения

3.1. Создание и активация виртуального окружения Python:

```
python -m venv venv
venv\Scripts\activate
```

3.2. Установка пакетов:

```
pip install -r requirements.txt
```

3.3. Генерация на основе protobuf-файлов:

```
python generate_proto.py
```

3.4. Запуск скрипта сервера:

```
python -m src.server
```

<img width="668" height="50" alt="3" src="https://github.com/user-attachments/assets/13c6bd7e-ec8b-4ef0-a71a-537375bad92f" />

3.5. Запуск скрипта клиента (в отдельном терминале):

```
python -m src.client
```

<img width="922" height="770" alt="4" src="https://github.com/user-attachments/assets/f2fc32e0-539d-41f1-a0d6-57cda030ed88" />
