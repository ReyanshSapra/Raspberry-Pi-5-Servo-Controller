import streamlit as st
from minio import Minio
from minio.error import S3Error
import io
from io import BytesIO
import time


client = Minio(
    endpoint="play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        secure=True
    )

uploadbool = False
client.remove_object("raspberrypi5servocontrollerreyansh", "servoCLOSE")
    
if st.button("Open Servo"):
    uploadbool = True

if st.button("Close Servo"):
    uploadbool = False

if uploadbool == True:
    if client.bucket_exists("raspberrypi5servocontrollerreyansh"):
        client.put_object("raspberrypi5servocontrollerreyansh", "servoMOVE", io.BytesIO(b""), length=0)

    else:
        client.make_bucket("raspberrypi5servocontrollerreyansh")
        client.put_object("raspberrypi5servocontrollerreyansh", "servoMOVE", io.BytesIO(b""), length=0)

    client.remove_object("raspberrypi5servocontrollerreyansh", "servoCLOSE")
    

if uploadbool == False:
    if client.bucket_exists("raspberrypi5servocontrollerreyansh"):
        client.put_object("raspberrypi5servocontrollerreyansh", "servoCLOSE", io.BytesIO(b""), length=0)

    else:
        client.make_bucket("raspberrypi5servocontrollerreyansh")
        client.put_object("raspberrypi5servocontrollerreyansh", "servoCLOSE", io.BytesIO(b""), length=0)

    client.remove_object("raspberrypi5servocontrollerreyansh", "servoMOVE")
        

