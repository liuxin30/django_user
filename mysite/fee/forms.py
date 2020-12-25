from django import forms
from .models import Info


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ["name", "id_num"]

        labels = {
            'name': "姓名",
            'id_num': "身份证号"
        }

    def clean(self):
        try:
            name = self.cleaned_data['name']
            id_num = self.cleaned_data['id_num']
        except KeyError:
            self.cleaned_data["message"] = "姓名或身份证号不能为空！请重新输入"
            raise forms.ValidationError('姓名或身份证号不能为空')
        else:
            info = Info.objects.get(name=name)
            if info.id_num != id_num:
                self.cleaned_data["message"] = "姓名或身份证号错误！请重新输入"
                raise forms.ValidationError('姓名或身份证号错误')
            self.cleaned_data["fee"] = info.fee
        return self.cleaned_data
