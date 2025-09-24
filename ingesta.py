import boto3

ficheroUpload = "data.csv"
nombreBucket = "gcr-output-01"

s3 = boto3.client('s3') #Libreria para conectarse a aws
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)
print(response)

print("Ingesta completada")