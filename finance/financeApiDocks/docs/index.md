# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

# Api
##Wallet
/api/wallet
```
{
    "name": String
    "amount": String
    "Owner": int
}
```
###post
Запрос с методом post Создает кошелек с именем name, суммой amount и владельцем Кошелька Owner

/api/wallet
```
{
    "name": String
    "amount": String
    "Owner": int
}
```
###put
Запрос с методом put прибавит число amount к сумме. Если число amount отрциательное и его сумма с изначальным значением меньше нуля, то запрос не выполнится 

##History
/api/history/
```
   {
        "data": "2021-04-15T00:00:00Z",
        "sum": "94408.000000",
        "wallet": 2,
        "typeOfTransaction": "replenishment",
        "description": "",
        "id": 19
    }
```
###get
Запрос с методом get вернет список всех транзакций

###
/api/history/id
###delete
Метод delete удаляет кошелек с заданным индексом
