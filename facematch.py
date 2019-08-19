import face_recognition

image_of_bill = face_recognition.load_image_file('./img/known/bill_Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

unknown_image = face_recognition.load_image_file('./img/unknown/bg.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

#compare faces
result = face_recognition.compare_faces([bill_face_encoding], unknown_face_encoding)

if result[0]:
    print("Bu Bill Gates'dir")
else :
    print("Bu Bill Gates değildir")