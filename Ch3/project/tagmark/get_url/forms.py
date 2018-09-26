from django import forms
from .models import Bookmark, Tag

class BookmarkForm(forms.Form):
    url = forms.URLField(label='URL 등록', required=True, max_length=250 )
    tag = forms.CharField(label='Tag 등록', required=True, max_length=250)
    def __init__(self, *args, **kwargs):
        """Init"""
        super(BookmarkForm, self).__init__(*args, **kwargs)
        self.fields['url'].widget.attrs['maxlength'] = 250
        self.fields['url'].widget.attrs['class'] = 'form-control'
        self.fields['url'].widget.attrs['placeholder'] = 'URL 붙여넣기'

        self.fields['tag'].widget.attrs['maxlength'] = 250
        self.fields['tag'].widget.attrs['class'] = 'form-control'
        self.fields['tag'].widget.attrs['placeholder'] = '태그는 쉼표로 구분'

    def clean_tag(self):
        tags = self.cleaned_data["tag"]

        if len(tags.split(",")) < 2:
            raise forms.ValidationError( "2개 이상 태그 & 쉼표로 구분.", code="tag" )
        return tags


    def save(self):
        bookmark = Bookmark.objects.create(url=self.cleaned_data["url"])

        for each in self.cleaned_data["tag"].split(","):
            try:
                tag = Tag.objects.get(text=each)
            except Exception as e:
                print(e)
                tag = Tag.objects.create(text=each)

            bookmark.tag.add(tag)

        bookmark.save()




