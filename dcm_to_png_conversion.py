"""
This code will help to convert dcm image to png image
pip install pydicom ; pypng
"""
import pydicom
import pypng

if dicom_filename.endswith('.dcm'):
    dicom_filename = 'dcm/image/path'
    (".dcm file Detected, Converting dcm to png..",dicom_filename)
    png_filename = os.path.splitext(dicom_filename)[0]
    suffix = '.png'
    png_filename = os.path.join(png_filename + suffix)
    bitdepth=16
    image = pydicom.read_file(dicom_filename).pixel_array
    with open(png_filename), 'wb') as f:
        writer = png.Writer(height=image.shape[0], width=image.shape[1], bitdepth=bitdepth, greyscale=True)
        writer.write(f, image.tolist())
