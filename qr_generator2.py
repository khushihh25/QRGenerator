import qrcode
from PIL import Image
import qrcode.constants

qr= qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=10,border=4)
qr.add_data("https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150")
qr.make(fit=True)
img =qr.make_image(fill_color ="red",back_color="blue")
img.save("leetcode11.png")