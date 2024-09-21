from io import BytesIO
import ddddocr
from PIL import Image

# 过点选验证码
# author: github.com/cv-cat
class DetectCaptcha:
    def __init__(self):
        self.detectOcr = ddddocr.DdddOcr(det=True, show_ad=False)
        self.commonOcr = ddddocr.DdddOcr(show_ad=False)

    def detectClickImg(self, imageContent):
        imageDict = dict()
        poses = self.detectOcr.detection(imageContent)
        img = Image.open(BytesIO(imageContent))
        for box in poses:
            x1, y1, x2, y2 = box
            corp = img.crop(box)
            img_byte = BytesIO()
            corp.save(img_byte, 'png')
            word = self.commonOcr.classification(img_byte.getvalue())
            imageDict[word] = [int((x1 + x2) / 2), int((y1 + y2) / 2)]
        return imageDict

    # 识别图片验证码数字
    def detectImg(self, imageContent):
        result = self.commonOcr.classification(imageContent)
        return result


if __name__ == '__main__':
    detectCaptcha = DetectCaptcha()
    # imageContent = open('../test.jpg', 'rb').read()
    # imageDict = detectCaptcha.detectClickImg(imageContent)
    # print(imageDict)

    imageContent = open('../1.jpeg', 'rb').read()
    result = detectCaptcha.detectImg(imageContent)
    print(result)