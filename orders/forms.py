from pathlib import Path

from django import forms

from .models import Order
from services.models import Service


MAX_FILES = 5
MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE = MAX_FILE_SIZE_MB * 1024 * 1024
MAX_TOTAL_UPLOAD_SIZE_MB = 15
MAX_TOTAL_UPLOAD_SIZE = MAX_TOTAL_UPLOAD_SIZE_MB * 1024 * 1024
ALLOWED_FILE_EXTENSIONS = {
    '.ai', '.doc', '.docx', '.jpeg', '.jpg', '.pdf', '.png', '.psd', '.rar', '.txt', '.webp', '.zip'
}


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    widget = MultipleFileInput

    def clean(self, data, initial=None):
        if not data:
            return []

        files = data if isinstance(data, (list, tuple)) else [data]
        if len(files) > MAX_FILES:
            raise forms.ValidationError(f'Можно загрузить не больше {MAX_FILES} файлов.')

        total_size = sum(file.size for file in files)
        if total_size > MAX_TOTAL_UPLOAD_SIZE:
            raise forms.ValidationError(
                f'Общий размер файлов не должен превышать {MAX_TOTAL_UPLOAD_SIZE_MB} МБ.'
            )

        cleaned_files = []
        for uploaded_file in files:
            cleaned_file = super().clean(uploaded_file, initial)
            if not cleaned_file:
                continue

            extension = Path(cleaned_file.name).suffix.lower()
            if extension not in ALLOWED_FILE_EXTENSIONS:
                allowed = ', '.join(sorted(ALLOWED_FILE_EXTENSIONS))
                raise forms.ValidationError(f'Можно загружать только файлы форматов: {allowed}.')

            if cleaned_file.size > MAX_FILE_SIZE:
                raise forms.ValidationError(f'Размер одного файла не должен превышать {MAX_FILE_SIZE_MB} МБ.')

            cleaned_files.append(cleaned_file)

        return cleaned_files


class OrderCreateForm(forms.ModelForm):
    files = MultipleFileField(
        required=False,
        label='Материалы к заказу',
        help_text=f'До {MAX_FILES} файлов, по {MAX_FILE_SIZE_MB} МБ каждый, всего до {MAX_TOTAL_UPLOAD_SIZE_MB} МБ.',
        widget=MultipleFileInput(attrs={
            'class': 'form-control',
            'multiple': True,
        })
    )

    class Meta:
        model = Order
        fields = ['service', 'title', 'description', 'contact']
        labels = {
            'service': 'Услуга',
            'title': 'Название заказа',
            'description': 'Техническое задание',
            'contact': 'Контакт для связи',
        }
        widgets = {
            'service': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Баннер для Telegram-канала'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Опиши стиль, размеры, текст, референсы и пожелания'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '@username, email или телефон'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.filter(is_active=True)
        self.fields['service'].empty_label = 'Выбери услугу'
