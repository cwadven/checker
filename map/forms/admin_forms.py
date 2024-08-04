from common.common_forms.admin_forms import PreSignedUrlAdminForm
from django import forms
from map.models import Map


class MapAdminForm(PreSignedUrlAdminForm):
    main_image_file = forms.ImageField(required=False)

    class Meta:
        model = Map
        fields = '__all__'
        target_field_by_image_field = {
            'main_image_file': 'main_image_url'
        }
        upload_image_type = 'map_main_image'
