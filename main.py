import traceback

quality_dict = {"1": 75, "2": 95, "3": 50, "4": 40}


def welcome():
    print("请选择需要压缩的类型：1:压缩excel 2:压缩图片")
    select_type = input("输入1选择压缩excel,输入2选择压缩图片，输入完成后按 '回车键' 确认:")
    temp_type = (int(select_type))
    print('请选择文件中图片压缩效果:')
    print('    1 最优(推荐!! 质量较好，图片文件压缩后文件大小变小)')
    print('    2 原样(质量不变、图片文件压缩后文件大小)')
    print('    3 中等(质量较差，图片文件压缩后文件大小较小)')
    print('    4 最差(压缩后质量较差，图片文件压缩后文件大小最小)')
    quality_input = input("请选择图片压缩效果,默认为 1:")
    if not quality_input:
        quality = quality_dict.get('1')
    else:
        if quality_input in {'1', '2', '3', '4'}:
            quality = quality_dict.get(quality_input)
        else:
            quality = quality_dict.get('1')
    print(quality)

    print('请输入文件中压缩后图片的最长边的像素大小:')
    print('    很绕是不是 ? 假如一张图片原始分辨率为 4000*3000 像素，那这张图片的最长边为宽，长度为 4000 像素')
    print('    我想要得到图片的分辨率为 400 * 300 像素的图片，我在输入框中输入400(最长边为宽，长度为 400 像素)')
    print('    就能得到一张图片压缩到 400 * 300 像素的图片')
    max_input = input("请输入压缩后图片的最长边的像素大小：")
    max_length = int(float(max_input))
    print(max_length)
    if temp_type == 1:
        print('请输入需要压缩的 excel 文件路径(绝对路径):')
        print('    也可以将 excel 文件拖到这个窗口')
        input_path = input("完成后按 '回车' 确认：")

        print('请输入压缩后的 excel 文件保存路径(绝对路径):')
        print('    也可以将需要存放的文件夹拖到这个窗口')
        output_path = input("完成后按 '回车' 确认：")
        import excel
        compress_path = excel.compress(input_path, output_path, max_length, quality)
        print("excel 文件中图片压缩成功，excel 保存路径:")
        print(compress_path)
    elif temp_type == 2:
        print('请输入需要压缩图片夹文件夹路径(绝对路径):')
        print('    也可以将文件拖到这个窗口')
        input_path = input("完成后按 '回车' 确认：")

        print('请输入压缩后的图片文件保存路径(绝对路径):')
        print('    也可以将需要存放的文件夹拖到这个窗口')
        output_path = input("    完成后按 '回车' 确认：")

        print('请确认是否将 png 转为 jpg格式，更节省空间:')
        print('    "1":"是，表示将png转为jpg"')
        print('    "2":"否，表示将png保持为原格式"')
        input_is_jpg = input("    完成后按 '回车' 确认:")
        temp_is_jpg = int(input_is_jpg)
        isSaveJpg = False
        if temp_is_jpg == 1:
            isSaveJpg = True

        import photo
        compress_path = photo.compressImage(input_path, output_path, False,
                                            max_length, isSaveJpg, quality)
        print("所有图片压缩成功，保存路径:")
        print(output_path)


if __name__ == '__main__':
    print("----------欢迎使用小仙女专用压缩工具----------")
    print("------------本工具版权归仙女所有-------------")
    print("-----------感谢灿小姐全程赞助，比心-------------")
    print('')
    print(r' ____  __   __  ____  _  _     ___  __   _  _  ____  ____  ____  ____  ____')
    print(r'(  __)/ _\ (  )(  _ \( \/ )   / __)/  \ ( \/ )(  _ \(  _ \(  __)/ ___)/ ___)')
    print(r' ) _)/    \ )(  )   / )  /   ( (__(  O )/ \/ \ ) __/ )   / ) _) \___ \\___ \ ')
    print(r'(__) \_/\_/(__)(__\_)(__/     \___)\__/ \_)(_/(__)  (__\_)(____)(____/(____/')
    print('')
    try:
        welcome()
    except:
        traceback.print_exc()
        print("哦吼，出错了！1 、2 、3 、4，再来一次")
        print()
        print()
        welcome()
