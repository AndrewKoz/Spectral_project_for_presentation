# Файл с путями до спектральных изображений.

from spectral import *

LDPE = open_image('Hyperspectral images/ПВД/results/REFLECTANCE_2021-11-24_003.hdr')  # Не имеет особенности в 930
PVC = open_image('Hyperspectral images/ПВХ/results/REFLECTANCE_2021-11-24_008.hdr')  # Не имеет особенности в 930
HDPE = open_image('Hyperspectral images/ПНД/results/REFLECTANCE_2021-11-24_007.hdr')  # Вот этот выделяется
PS = open_image('Hyperspectral images/Полистирол/results/REFLECTANCE_2021-11-24_004.hdr')  # Не имеет особенности в 930
PP = open_image('Hyperspectral images/ПП/results/REFLECTANCE_2021-11-24_006.hdr')  # Корзинка и лего имеют особенность в 930
PET = open_image('Hyperspectral images/ПЭТ пленка/results/REFLECTANCE_2021-11-24_005.hdr')  # Не имеет особенности в 930

plastic_name_to_image = {'LDPE': LDPE, 'PVC': PVC, 'HDPE': HDPE, 'PS': PS, 'PP': PP, 'PET': PET}
