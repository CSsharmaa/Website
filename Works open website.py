import webbrowser as web

import speech_recognition as sr


def main():
    path = "C:/Program Files (x86)/Google/Update/Download/{8A69D345-D564-463C-AFF1-A69D9E530F96}/96.0.4664.45/96.0.4664.45_chrome_installer.exe %s"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something ")

        audio = r.listen(source)

        print("Recognizing Now ... ")

        try:
            dest = r.recognize_google(audio)
            print("You have said : " + dest)

            web.get(path).open(dest)

        except Exception as e:
            print("Error : " + str(e))


if __name__ == "__main__":
    main()
