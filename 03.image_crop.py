import cv2

if __name__ == "__main__": 
    color_img = cv2.imread("./Lenna.png", cv2.IMREAD_COLOR)
    cropped_img = color_img[0:color_img.shape[0]//2, 0:color_img.shape[1]//2]

    if cv2.imwrite("./cropped_img.jpg", cropped_img): 
        print("저장 완료")
        print(f"원본: {color_img.shape}") # 원본: (512, 512, 3)
        print(f"크롭: {cropped_img.shape}") # 크롭: (256, 256, 3)
    else: 
        print('저장 출력') 