# TpCryptoHw7
В данном репозитории представлена реализация домашнего задания 5 по курсу криптографии в технопарке mail.ru - реализация схемы Шамира разделения секрета. Из-за ограничений библиотеки **pycryptodome программа работает только с 128-битными ключами**. Launch.png содержит скриншот запуска программы.
## Запуск программы
Перед запуском необходимо установить библиотеку pycryptodome
```
$ pip install pycryptodome
```
После этого необходимо вызвать программу с указанием режима работы (generate, splitm, recover)
- Windows:
```
python main.py split
```
- Linux (не тестировалась):
```
./main.py split
```
## Тесты и режимы работы
- Режим generate позволяет сгенерировать случайный 128-битный ключ
```
>python main.py generate
=== WELCOME TO SHAMIR SPLITTER ===

Generated key:
0xe14ae88266bc5682d2b994deba903a54
```
- Режим split разделяет заданный ключ на N частей, T из которых необходимы для восстановления
```
>python main.py split
=== WELCOME TO SHAMIR SPLITTER ===

Input secret:
0xe14ae88266bc5682d2b994deba903a54

Input N T (N >= T):
5 2

Splitted secret:
Part 1: 0x01b70999e53df86ad1be5bf94bd91c7d
Part 2: 0x20b12ab561bf0b52d4b60a9158027681
Part 3: 0xc04ccbaee23ea5bad7b1c5b6a94b50a8
Part 4: 0x62bd6cec68baed22dea6a8417fb4a379
Part 5: 0x82408df7eb3b43cadda167668efd8550
```
- Режим recover обеспечивает восстановление исходного ключа по T или большему числу частей (для выхода из режима ввода нужно ввести пустую строку)
```
>python main.py recover
=== WELCOME TO SHAMIR SPLITTER ===

Input idx and part of secret separated by ":" (or press enter to exit):
1: 0x01b70999e53df86ad1be5bf94bd91c7d
4: 0x62bd6cec68baed22dea6a8417fb4a379

0xe14ae88266bc5682d2b994deba903a54
```
*Можно видеть, что восстановленный ключ совпадает с исходным* 