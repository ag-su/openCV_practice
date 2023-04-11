import cv2

if __name__ == "__main__": 
    color_img = cv2.imread("./Lenna.png", cv2.IMREAD_COLOR)
    resized_img = cv2.resize(color_img, (1024, 1024))

    if cv2.imwrite("./resized_img.jpg", resized_img): 
        print("저장 완료")
        print(f"원본: {color_img.shape}") # 원본: (512, 512, 3)
        print(f"크기 조정: {resized_img.shape}") # 크기 조정: (1024, 1024, 3)
    else: 
        print('저장 출력') 