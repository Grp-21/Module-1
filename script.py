import piexif
#this script and image should be in same file and image name here
exif_dict = piexif.load("sample.jpg")
thumbnail = exif_dict.pop("thumbnail")
if thumbnail is not None:
    with open("thumbnail.jpg", "wb+") as f:
        f.write(thumbnail)
        
#for printing the whole exif_dict
"""        
for ifd_name in exif_dict:
    print("\n{0} IFD:".format(ifd_name))
    for key in exif_dict[ifd_name]:
        try:
            print(key, exif_dict[ifd_name][key][:10])
        except:
            print(key, exif_dict[ifd_name][key])
"""            
gps_info = exif_dict['GPS']
GPSLatitude = gps_info[2]
GPSLongitude = gps_info[4]
Latitude_direction = gps_info[1].decode('utf-8')
Longitude_direction = gps_info[3].decode('utf-8')

#for converting to decimal from degrees minutes seconds
def get_decimal_from_dms(dms, ref):
    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0
    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds
    return round(degrees + minutes + seconds, 5)

def get_coordinates():
    lat = get_decimal_from_dms(GPSLatitude,Latitude_direction)
    lon = get_decimal_from_dms(GPSLongitude,Longitude_direction)
    return (lat,lon)
print(get_coordinates())



