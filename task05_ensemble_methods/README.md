## **Набор данных содержит следующие столбцы:**

* model: модель автомобиля 
* year: год изготовления 
* price: цена автомобиля 
* transmission: тип коробки передач 
* mileage: пробег автомобиля 
* fuelType: тип топлива, которое использует автомобиль 
* tax: налог 
* mpg: мили на галлон, мера топливной эффективности 
* engineSize: размер двигателя 
* Manufacturer: производитель автомобиля 

### **Набор данных содержит 97 712 записей и ни одного пропущенного значения во всех столбцах. Вот краткое изложение ключевых числовых характеристик:**

* Год: автомобили выпускаются с 1970 по 2024 год, средний год — 2017, что указывает на относительно современный набор автомобилей.
* Цена: цены варьируются от 450 до 159 999 фунтов стерлингов, средняя цена составляет 14 470 фунтов стерлингов.
* Пробег: пробег значительно варьируется: от 1 до 323 000 миль, в среднем 17 682,5 миль.
* Налог: годовая ставка налога колеблется от 0 до 580 фунтов стерлингов, в среднем 145 фунтов стерлингов.
* MPG (миль на галлон): топливная экономичность колеблется от 0,3 до 470,8 миль на галлон, в среднем 54,3 миль на галлон.
* Размер двигателя: объем двигателя варьируется от 0 (возможно, указывает на электромобили) до 6,6 литров со средним объемом 1,6 литра.

### **Распределение категориальных переменных дает представление о составе набора данных:**

* Типы трансмиссий: набор данных преимущественно содержит автомобили с механической коробкой передач (55 502), за которыми следуют полуавтоматические (22 296) и автоматические (19 905). Есть несколько записей, помеченных как «Другое» (9), которые могут относиться к особым случаям или ошибкам.
* Виды топлива: большинство автомобилей используют бензин (53 982), за ним следует дизельное топливо (40 419). Существуют также гибридные (3059), другие (246) и электрические (6) транспортные средства, в которых используется широкий спектр типов топлива.
* Производители: в число крупнейших производителей, представленных в наборе данных, входят Ford (17 811), Volkswagen (14 893), Vauxhall (13 258), Mercedes (12 860) и BMW (10 664). Это говорит о разнообразии брендов со значительным присутствием европейских производителей.

### **Матрица корреляции числовых характеристик в наборе данных выявляет несколько ключевых взаимосвязей:**

* Цена и год: существует умеренная положительная корреляция (0,49) между ценой автомобиля и годом его выпуска, что указывает на то, что новые автомобили, как и ожидалось, имеют тенденцию стоить выше.
* Цена и пробег: как и ожидалось, существует отрицательная корреляция (-0,40) между ценой и пробегом. Больший пробег обычно приводит к снижению цен.
* Цена и объем двигателя: существует сильная положительная корреляция (0,66) между ценой и объемом двигателя, что позволяет предположить, что автомобили с более мощными двигателями обычно стоят дороже.
* Пробег и год: существует значительная отрицательная корреляция (-0,78) между пробегом и годом, показывающая, что новые автомобили, как правило, имеют меньший пробег.
* Налог и расход миль на галлон: существует незначительная отрицательная корреляция (-0,35) между налогом и расходом миль на галлон, что указывает на небольшую тенденцию для более экономичных автомобилей иметь более низкие налоги.