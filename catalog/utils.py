from firebase_admin import storage

def upload_image_to_firebase(image_file):
   # Get a reference to the Firebase Storage bucket
   bucket = storage.bucket()
   
   # Create a blob (file) reference with a unique name
   blob = bucket.blob(f'images/{image_file.name}')
   
   # Upload the image file to Firebase
   blob.upload_from_file(image_file)

   # Make the image publicly accessible (optional)
   blob.make_public()

   # Get the URL of the uploaded image
   return blob.public_url