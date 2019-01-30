from wand.image import Image
import os

from utilities.common import utc_now_timestamp as now
from settings import UPLOAD_FOLDER


def thumbnail_process(file, content_type, content_id, sizes=[("sm", 50), ("lg", 75), ("xlg", 200)]):
    image_id = now()
    filename_template = content_id + '.%s.%s.png'

    # original
    with Image(filename=file) as img:
        crop_center(img)
        img.format = 'png'
        img.save(filename=os.path.join(UPLOAD_FOLDER, content_type, filename_template % (image_id, 'raw')))

    # sizes
    for (name, size) in sizes:
        with Image(filename=file) as img:
            crop_center(img)
            img.sample(size, size)
            img.format = 'png'
            img.save(filename=os.path.join(UPLOAD_FOLDER, content_type, filename_template % (image_id, name)))

    os.remove(file)
    return image_id


def crop_center(image):
    width_less_than_height = 1 > image.width / image.height
    square_side = image.width if width_less_than_height else image.height
    image.crop(
        left=int((image.width - square_side) / 2),
        top=int((image.height - square_side) / 2),
        width=int(square_side),
        height=int(square_side)
    )
