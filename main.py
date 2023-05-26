def proc3():
    import csv
    with open('123.csv', encoding='utf=8') as File:
        reader = csv.reader(File)
        k = 0
        total_cost = 0
        for row in reader:
            if k == 0:
                print('Нужно купить:')
            else:
                item_name = row[0]
                quantity = int(row[1])
                price_per_unit = int(row[2])

                print(f'{item_name} - {quantity} шт. за {price_per_unit} руб.')
                total_cost += quantity * price_per_unit
            k += 1
        print('Итоговая сумма:', total_cost)



def proc2():
    from PIL import Image, ImageFilter
    from pathlib import Path

    current_dir =''
    filenames = Path(current_dir).glob('*')
    Path('new_dir').mkdir(exist_ok=True)

    for file in filenames:
        if file.suffix in ['.jpg','.png']:
            with Image.open(file) as img:
                img.load()
                new_img = img.filter(ImageFilter.EMBOSS)
                new_img.save(Path("new_dir",file))

proc3()