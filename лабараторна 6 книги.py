із  колекцій  імпортувати  namedtuple

 Бібліотека класів ( об'єкт ):
    def  __init__ ( self ):
        себе . книги  = []

    def  addBook ( self , book ):
        себе . книги . додати ( книга )

    Захист   searchBookYear ( самостійно , рік ):
        для  книги  в  собі . книги :
            якщо  книга . рік  ==  рік :
                повернути  книгу

    Захист  searhBookAuthor ( самостійно , автор ):
        wrote_by_author  = []
        для  книги  в  собі . книги :
            якщо  книга . автор  ==  автор :
                wrote_by_author . додати ( книга )
        повернути  write_by_author

    def  searchUnderPrice ( власний , ціна ):
        books_under_price  = []
        для  книги  в  собі . книги :
            якщо  книга . ціна  <  ціна :
                books_under_price . додати ( книга )
        повернути  books_under_price


Book  =  namedtuple ( 'Книга' , 'назва автора рік' )

library  =  Бібліотека ()
бібліотека . addBook ( Книга ( 'Идиот' , 'Достоевский Федор Михайлович' , '1869' , 40 ))
бібліотека . addBook ( Книга ( 'Цветы для Элджернона' , 'Дэниел Киз' , '1958 ' , 30 ))
бібліотека . addBook ( Книга ( '451 градус по Фаренгейту' , 'Рэй Брэдбери' , '1953' , 25 ))
бібліотека . addBook ( Книга ( 'мойсей' , 'Иван Яковлевич Франко' , '1905' , 15 ))
друк ( бібліотека . searchBookYear ( '1937' ))
