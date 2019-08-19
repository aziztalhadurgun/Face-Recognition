import face_recognition

image = face_recognition.load_image_file('./img/group/team5.jpg')
face_locations = face_recognition.face_locations(image)

#arrayde yüzlerin koordinatları
#print(face_locations)

print(f'bu resimde {len(face_locations)} adet yüz var')
