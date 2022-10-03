def brightness_contrast(img, a, b):
    img = img*a+b
    if (len(img.shape) > 1):
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i][j] < 0:
                    img[i][j] = 0
                elif img[i][j] > 255:
                    img[i][j] = 255
                else:
                    img[i][j] = img[i][j]
    else:
        for i in range(len(img)):
            if img[i] < 0:
                img[i] = 0
            elif img[i] > 255:
                img[i] = 255
            else:
                img[i] = img[i]

    return img



