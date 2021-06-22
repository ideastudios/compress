import os
import traceback

from PIL import Image


# 图片压缩批处理
def compressImage(srcPath, dstPath, isDelete, maxLength: int, isSaveJpg, quality):
    for filename in os.listdir(srcPath):
        # 如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
            os.makedirs(dstPath)

        # 拼接完整的文件或文件夹路径
        srcFile = os.path.join(srcPath, filename)
        if isSaveJpg:
            format = "JPEG"
            newname = os.path.splitext(filename)[0] + ".jpg"
        else:
            format = filename.split('.')[-1].upper()
            newname = filename

        dstFile = os.path.join(dstPath, newname)

        # 如果是文件就处理
        if os.path.isfile(srcFile):
            # if os.path.getsize(srcFile) < 100 * 1024 * 1024:
            #     continue
            try:
                # 打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
                sImg = Image.open(srcFile)
                w, h = sImg.size
                ratio = 1
                if maxLength:
                    image_max_length = int(max(int(w), int(h)))
                    if image_max_length > maxLength:
                        ratio = image_max_length / maxLength

                dImg = sImg.resize((int(w / ratio), int(h / ratio)), Image.ANTIALIAS)  # 设置压缩尺寸和选项，注意尺寸要用括号
                if isDelete:
                    os.remove(srcFile)
                if isSaveJpg:
                    print("convert")
                    dImg.convert('RGB')
                dImg.save(dstFile, format=format, quality=quality)

            except Exception:
                traceback.print_exc()

        # 如果是文件夹就递归
        if os.path.isdir(srcFile):
            compressImage(srcFile, dstFile)


if __name__ == "__main__":
    print("hahahaha")
    src_path = './media'
    des_path = './haha'
    compressImage(src_path, des_path, False, 0, True, 75)
