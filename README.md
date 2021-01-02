## Сбор и анализ данных по аренде недвижимости в Казани

В данной работе собираются и анализируются данные по аренде квартир в Казани с сервиса для поиска недвижимости [Циан](http://cian.ru)

#### Признаки, получаемые в ходе парсинга.
* how_many_rooms - количество комнат, от 1 до 4х
* price_per_month - стоимость аренды в месяц
* street - улица, в которой расположена квартира
* district - район, в которой расположена квартира
* floor - этаж, на котором расположена квартира
* all_floors - общее количество этажей в здании, на котором расположена квартира
* square_meters - общее количество квадратных метров
* commissions - коммиссиия, взымаемая в ходе первичной аренды
* author - автор поста
* year_of_construction - год постройки здания, на котором расположена квартира
* comm_meters - количество жилых квадратных метров
* kitchen_meters - количество квадратных метров кухни
* link - ссылка на это объявление

В некоторых объявлениях отсутсвуют данные по некоторым признакам (год постройки, жилые кв метры, кв метры кухни).
В этом случае проставляется значение -1.

В небольшом первичном исследовании рассматриваются следующие вопросы:

*В каких районах больше всего предложений*

*Распределение цен на квадратный метр в среднем по Казани*

*Распределение предложений в завизимости от даты постройки здания*

*Распределение цен в трёх категориях: до 1975х, между 1975 и 2010, и после*

*Распределение цен на квадратный метр в зависимости от количества комнат*

*Распределение цен аренды на квадратный метр в зависимости от районов для всех годов постройки*

*Распределение цен аренды на квадратный метр в зависимости от районов для годов постройки > 2000*

*Распределение цен на квадратный метр в зависимости от количества комнат в среднем во всех районов*

*Распределение цен на квадратный метр в зависимости от этажности квартиры*
