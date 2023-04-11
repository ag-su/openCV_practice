import cv2

if __name__ == "__main__": 
    color_img = cv2.imread("./Lenna.png", cv2.IMREAD_COLOR)
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY) # openCV는 기본적으로 BGR로 읽음 

    if cv2.imwrite("./converted_to_gray.jpg", gray_img): 
        print("저장 완료")
    else: 
        print('저장 출력') 