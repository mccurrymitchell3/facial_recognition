from PIL import Image, ImageDraw
import face_recognition

# Load the image file into a numpy array
image = face_recognition.load_image_file("me.jpg")
height, width = image.shape[0], image.shape[1]

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

# Load the image into a Python Image Library object so that we can draw on top of it and display it
pil_image = Image.fromarray(image)

# Create a PIL drawing object to be able to draw lines later
d = ImageDraw.Draw(pil_image, 'RGBA')

for face_landmarks in face_landmarks_list:
    # The face landmark detection model returns these features:
    # chin, left_eyebrow, right_eyebrow, nose_bridge, nose_tip, left_eye, right_eye, top_lip, bottom_lip

    # Draw clown nose
    xy = ((face_landmarks["nose_bridge"][2][0]-width*.055, face_landmarks["nose_bridge"][2][1]-height*.01), (face_landmarks["nose_bridge"][3][0]+width*.055, face_landmarks["nose_bridge"][3][1]+height*.025))
    d.ellipse(xy, fill=(255, 0, 0))

# Show the final image
pil_image.show()
