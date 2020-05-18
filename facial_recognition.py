import face_recognition

# Load the known images
tony = face_recognition.load_image_file("sopranos/people/tony.jpg")
silvio = face_recognition.load_image_file("sopranos/people/silvio.jpg")
christopher = face_recognition.load_image_file("sopranos/people/christopher.jpg")
pauly = face_recognition.load_image_file("sopranos/people/pauly.jpg")
carmine = face_recognition.load_image_file("sopranos/people/carmine.jpg")
ralph = face_recognition.load_image_file("sopranos/people/ralph.jpg")
furio = face_recognition.load_image_file("sopranos/people/furio.png")
johnny = face_recognition.load_image_file("sopranos/people/johnny.jpg")

# Get the face encoding of each person. This can fail if no one is found in the photo.
tony_face_encoding = face_recognition.face_encodings(tony)[0]
silvio_face_encoding = face_recognition.face_encodings(silvio)[0]
christopher_face_encoding = face_recognition.face_encodings(christopher)[0]
pauly_face_encoding = face_recognition.face_encodings(pauly)[0]
carmine_face_encoding = face_recognition.face_encodings(carmine)[0]
ralph_face_encoding = face_recognition.face_encodings(ralph)[0]
furio_face_encoding = face_recognition.face_encodings(furio)[0]
johnny_face_encoding = face_recognition.face_encodings(johnny)[0]

# Create a list of all known face encodings
known_face_encodings = [
    tony_face_encoding,
    silvio_face_encoding,
    christopher_face_encoding,
    pauly_face_encoding,
    carmine_face_encoding,
    ralph_face_encoding,
    furio_face_encoding,
    johnny_face_encoding
]

# Load the image we want to check
unknown_image = face_recognition.load_image_file("sopranos/sopranos_6.jpg")

# Get face encodings for any people in the picture
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

# There might be more than one person in the photo, so we need to loop over each face we found
for unknown_face_encoding in unknown_face_encodings:

    # Test if this unknown face encoding matches any of the three people we know
    results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding, tolerance=0.6)

    name = "Unknown"

    if results[0]:
        name = "Tony"
    elif results[1]:
        name = "Silvio"
    elif results[2]:
        name = "Christopher"
    elif results[3]:
        name = "Pauly"
    elif results[4]:
        name = "Carmine"
    elif results[5]:
        name = "Ralph"
    elif results[6]:
        name = "Furio"
    elif results[7]:
        name = "Johnny"

    print(f"Found {name} in the photo!")
