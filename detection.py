import cv2

try:
    face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    hat = cv2.imread('Filters\\hat.png')
    glass = cv2.imread('Filters\\Converted\\glasses.png')
    glass2 = cv2.imread('Filters\\Frames\\glasses2.png')
    glass3 = cv2.imread('Filters\\Frames\\glasses3.png')
    glass4 = cv2.imread('Filters\\Frames\\glasses42.png')
    glass5 = cv2.imread('Filters\\Frames\\glasses52.png')
    glass6 = cv2.imread('Filters\\Frames\\glasses6.png')
    fun = cv2.imread('Filters\\Frames\\fun.png')
    bunny = cv2.imread('Filters\\Frames\\bunny.png')
    cig = cv2.imread('Filters\\Frames\\c3.png')


    # def put_dog_filter(dog, fc, x, y, w, h):
    #     face_width = w
    #     face_height = h
    #
    #     dog = cv2.resize(dog, (int(face_width * 1.5), int(face_height * 1.95)))
    #
    #     for i in range(int(face_height * 1.75)):
    #         for j in range(int(face_width * 1.5)):
    #             for k in range(3):
    #                 if dog[i][j][k] < 235:
    #                     fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = dog[i][j][k]
    #     return fc

    # Methods


    def put_hat(hat, fc, x, y, w, h):
        face_width = w
        face_height = h

        hat_width = face_width + 1
        hat_height = int(0.50 * face_height) + 1

        hat = cv2.resize(hat, (hat_width, hat_height))

        for i in range(hat_height):
            for j in range(hat_width):
                for k in range(3):
                    if hat[i][j][k] < 235:
                        fc[y + i - int(0.40 * face_height)][x + j][k] = hat[i][j][k]
        return fc


    def put_glass(glass, fc, x, y, w, h):
        face_width = w
        face_height = h

        hat_width = face_width + 1
        hat_height = int(0.50 * face_height) + 1

        glass = cv2.resize(glass, (hat_width, hat_height))

        for i in range(hat_height):
            for j in range(hat_width):
                for k in range(3):
                    if glass[i][j][k] < 235:
                        try:
                            fc[y + i - int(-0.20 * face_height)][x + j][k] = glass[i][j][k]
                        except IndexError:
                            break
                            print("Index Error")

        return fc


    def giveInp(inp):
        runVideo(inp)


    def multipleGlassChoicePicker(chosenGlass, frame, x, y, w, h):
        try:
            frame = put_glass(chosenGlass, frame, x, y, w, h)
        except KeyboardInterrupt:
            print('Terminated at Outro.')


    def multipleHatChoicePicker(chosenHat, frame, x, y, w, h):
        try:
            frame = put_glass(chosenHat, frame, x, y, w, h)
        except KeyboardInterrupt:
            print('Terminated at Outro.')


    def runVideo(selectedItem):
        choice = selectedItem
        # choice = 0
        # print('Enter your choice filter to launch that :\n1\t\t\t      : Glasses\n'
        #       'Other Number \t  : Glasses 2')
        # choice = int(input('Enter your choice : '))
        webCam = cv2.VideoCapture(0)
        while True:
            size = 4
            (rval, im) = webCam.read()
            im = cv2.flip(im, 1, 0)
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            fl = face.detectMultiScale(gray, 1.19, 7)

            for (x, y, w, h) in fl:
                # normal
                if choice == 1:
                    multipleGlassChoicePicker(glass, im, x, y, w, h)
                # blue aviators
                elif choice == 2:
                    multipleGlassChoicePicker(glass2, im, x, y, w, h)
                # rect
                elif choice == 3:
                    multipleGlassChoicePicker(glass3, im, x, y - 8, w, h)
                # circular not filled
                elif choice == 4:
                    multipleGlassChoicePicker(glass4, im, x, y, w, h)
                # circular filled
                elif choice == 5:
                    multipleGlassChoicePicker(glass5, im, x, y - 20, w, h)
                # cat eye
                elif choice == 6:
                    multipleGlassChoicePicker(glass6, im, x, y - 10, w, h)
                # fun
                elif choice == 7:
                    multipleGlassChoicePicker(fun, im, x, y - 15, w, h)
                    multipleGlassChoicePicker(cig, im, x + 74, y + 22, w, h)
                # bunny
                elif choice == 8:
                    multipleHatChoicePicker(bunny, im, x, y - 37, w, h)
                # cigarette
                elif choice == 9:
                    multipleHatChoicePicker(cig, im, x + 74, y + 22, w, h)
                # error
                else:
                    print("Out of bounds")
            cv2.imshow('ENIGMA', im)
            try:
                if cv2.waitKey(1) & 0xff == ord('q'):
                    break
            except IOError:
                print(Exception)
except KeyboardInterrupt:
    print('Terminated...')
# runVideo(0)
# giveInp()
# we need runcd() here to run this file without the use of main
