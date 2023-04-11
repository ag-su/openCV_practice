import cv2

if __name__ == "__main__": 
    color_img = cv2.imread("./Lenna.png", cv2.IMREAD_COLOR)
    gray_img = cv2.imread("./Lenna.png", cv2.IMREAD_GRAYSCALE)

    print(color_img.shape)
    print(gray_img.shape)

    if cv2.imwrite("./Lenna_gray.jpg", gray_img): 
        print("저장 완료")
    else: 
        print('저장 출력') 