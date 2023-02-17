#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = 8858279
    API_HASH = "ef28c3f458143cbcb4271a98a2e9d596"
    BOT_TOKEN = "5912998821:AAHnfwQMIgzQ5GgaAw1iyiDIts11pn2SKkY"
    DEV = 1322549723
    OWNER = "5371981851"
    FFMPEG = config(
        "FFMPEG",
       default='''ffmpeg -i "{}" -filter_complex "[0:v]drawtext=fontfile=font.ttf:text='t.me/animxt':fontsize=22:fontcolor=ffffff:alpha='if(lt(t,0),0,if(lt(t,5),(t-0)/5,if(lt(t,15),1,if(lt(t,20),(5-(t-15))/5,0))))':x=w-text_w-15:y=15" -s 1280x720 -c:v libx265 -preset medium -pix_fmt yuv420p10le -r 24000/1001 -crf 25 -x265-params deblock=-1,-1:no-sao:aq-mode=2:aq-strength=0.90:frame-threads=4:no-info=1 -c:a libopus -b:a 96k -map 0:a -c:s copy -map 0:s? "{}" -y''',
    )
    THUMB = config(
        "THUMBNAIL", default="www.google.com"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
