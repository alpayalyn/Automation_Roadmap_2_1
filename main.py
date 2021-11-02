# ogrenci bilgilerini iceren sınıf
class studentClass:
    def __init__(self, nameofStudent, surnameofStudent, classofStudent):
        self.nameofStudent = nameofStudent
        self.surnameofStudent = surnameofStudent
        self.classofStudent = classofStudent

    def showInformation(self):
        print(""" 
              nameofStudent : {}
              surnameofStudent : {}
              ogrenciSinif : {}
              """.format(self.nameofStudent, self.surnameofStudent, self.classofStudent))

# net sayisini hesaplar, net sayisi ile total puanı da hesaplar
class questions:
    @staticmethod
    def NetSayisi(correct, wrong):

            wrongplus = int(wrong /4)
            totalNet = correct - wrongplus
            print("""
                correctAnswerSayisi : {}
                wrongAnswerSayisi : {}
                ogrenciNetSayisi : {}
                """.format(correct, wrong, totalNet))
            return totalNet

    @staticmethod
    def calculate(totalNet):
        totalPoints = totalNet * 2
        print(""" 
              ogrencitotalPointsi : {}
              """.format(totalPoints))

studentName = input("Öğrenci ismi giriniz:")
studentSurname = input("Öğrenci soyismi giriniz:")
studentClassLocal = input("Öğrenci sinifini giriniz:")

# toplam 50 soru mu kontrolü
while True:
    correctAnswer = int(input("Öğrenci doğru sayısını giriniz:"))
    wrongAnswer = int(input("Öğrenci yanlış sayısını giriniz:"))

    if(correctAnswer + wrongAnswer != 50):
        print("Lütfen yanlış ve doğru toplamı 50 olacak şekilde doğru yanlış sayısını giriniz.")
    else:
        break

studentOutput = studentClass(studentName, studentSurname, studentClassLocal)
studentOutput.showInformation()

questionOutputs = questions()
totalNets = questionOutputs.NetSayisi(correctAnswer, wrongAnswer)
questionOutputs.calculate(totalNets)