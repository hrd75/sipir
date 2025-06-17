from django import forms
from .models import PostData
from datetime import datetime, timezone

#d = datetime ("%Y-%d-%m %H:%M:%S")

#datetime_obj = dateparse.parse_datetime(d)

#widgets = {
#    'waktu': forms.DateTimeField(datetime_obj) 
#}

#string_tanggal = "2024-6-16 9:53:0"
#format_tanggal = "YYYY-MM-DDTHH:mm:ss.sssZ"

#d = datetime.date()
#frodte = d.strftime("%d/%m/%y")

d = datetime(2014, 6, 15, 14, 30, 50, 321, tzinfo=timezone.utc)

class MenuUtama(forms.ModelForm):
    class Meta: 
        model = PostData
        fields = (
            'nama',
            'satker',
            'ruangan',
            'waktu',
            'keterangan',
        )

        TAHUN = range(1945, 2030, 1)

        widgets = {
            'waktu': forms.SelectDateWidget(years=TAHUN)
            
        }




