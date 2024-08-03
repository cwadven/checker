from common.common_utils import (
    generate_pre_signed_url_info,
    upload_file_to_pre_signed_url,
)
from django import forms


class PreSignedUrlAdminForm(forms.ModelForm):
    """
    Admin Form for handling pre-signed URL for image upload
    Need to define Meta class with 'mapping_image_fields' and 'upload_image_type'

    mapping_image_fields key: The field name in the form for the image file upload.
    mapping_image_fields value: The field name in the model for the image URL.
    upload_image_type: The type of image upload to folder of S3. Default is 'common'.

    examples:
    class XXXXForm(PreSignedUrlAdminForm):
        main_image_file = forms.ImageField(required=False)

        class Meta:
            model = XXXX
            fields = '__all__'
            mapping_image_fields = {
                'main_image_file': 'main_image_url'
            }
            upload_image_type = 'xxxx_main_image'
    """
    def _get_meta(self):
        return getattr(self, 'Meta')

    def _get_mapping_image_fields(self):
        return getattr(self._get_meta(), 'mapping_image_fields', {})

    def _get_upload_image_type(self):
        return getattr(self._get_meta(), 'upload_image_type', 'common')

    def save(self, commit=True):
        instance = super(PreSignedUrlAdminForm, self).save(commit=False)
        for key, value in self._get_mapping_image_fields().items():
            if self.cleaned_data[key]:
                response = generate_pre_signed_url_info(
                    self.cleaned_data[key].name,
                    _type=self._get_upload_image_type(),
                    unique=str(instance.id) if instance.id else '0'
                )
                upload_file_to_pre_signed_url(response['url'], response['fields'], self.cleaned_data[key].file)
                setattr(instance, value, response['url'] + response['fields']['key'])
        if commit:
            instance.save()
        return instance
