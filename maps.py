import cartopy.crs as ccrs
import matplotlib.pyplot as plt


def plate_draw():

    # Создание новой картинки с графиком, с использованием проекции PlateCarree
    ax = plt.axes(projection=ccrs.PlateCarree())

    # Добавление береговой линии к графику
    ax.coastlines()

    # Отображение графика
    plt.savefig("out.png")


def mall_draw():

    # Создание новой картинки с графиком, с использованием проекции PlateCarree
    ax = plt.axes(projection=ccrs.Mollweide())

    # Добавление береговой линии к графику
    ax.stock_img()

    # Отображение графика
    plt.savefig("out1.png")


if __name__=="__main__":
    plate_draw()
    mall_draw()