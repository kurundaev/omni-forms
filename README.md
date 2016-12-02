[![Omni Forms on pypi](https://img.shields.io/badge/pypi-0.1.0-green.svg)](https://pypi.python.org/pypi/omniforms)
![MIT license](https://img.shields.io/badge/licence-MIT-blue.svg)
![Build status](https://travis-ci.org/omni-digital/omni-forms.svg?branch=master)

# Omni Forms

Omni forms is a simple form builder with admin integration for django versions >= 1.8.

`pip install omniforms`

!Pypi release coming soon

Once the package has been installed just add `omni_forms` to `INSTALLED_APPS` in your settings file:

`INSTALLED_APPS += ('omni_forms',)`

Once you've done this run `python manage.py migrate` to migrate your database.

## Configuration

The OmniForms application can be configured in a number of different ways:

### Permitted content types

You may not want administrators to be able to create forms for _all_ different types of content in your database.  There are 2 different ways of restricting the types of content that can be associated with model forms created through the admin interface:


## OMNI_FORMS_CONTENT_TYPES

It is possible to define specific apps and/or models which can be used by the omniforms app using the `OMNI_FORMS_CONTENT_TYPES` setting.

For example:

The following configuration would allow _any_ of the models in the app `foo` and the `modelone` and `modeltwo` models within the `bar` app to be used.

```
OMNI_FORMS_CONTENT_TYPES = [
    {'app_label': 'foo'},
    {'app_label': 'bar', 'model': 'modelone'},
    {'app_label': 'bar', 'model': 'modeltwo'},
]
```

If the `OMNI_FORMS_CONTENT_TYPES` setting is not defined it will default to `None` and the `OMNI_FORMS_EXCLUDED_CONTENT_TYPES` setting will be used instead (default values or otherwise).


## OMNI_FORMS_EXCLUDED_CONTENT_TYPES

It is possible to prevent model forms from being created for specific apps or specific models using the `OMNI_FORMS_EXCLUDED_CONTENT_TYPES` setting.

For example:

The following configuration would prevent forms being created for _any_ of the models in the app `foo` and for the `modelone` and `modeltwo` models within the `bar` app.

```
OMNI_FORMS_EXCLUDED_CONTENT_TYPES = [
    {'app_label': 'foo'},
    {'app_label': 'bar', 'model': 'modelone'},
    {'app_label': 'bar', 'model': 'modeltwo'},
]
```

If you do not specify this setting it will default to the following:

```
OMNI_FORMS_EXCLUDED_CONTENT_TYPES = [
    {'app_label': 'omniforms'}
]
```

This will prevent administrators from creating form_builder forms with the formbuilder itself.
It's worth mentioning that allowing administrators to do this represents a potential security risk and should be avoided.
As such, if you need to define your own `OMNI_FORMS_EXCLUDED_CONTENT_TYPES` setting it would be wise to exclude all `omniforms` models as shown above.


## OMNI_FORMS_CUSTOM_FIELD_MAPPING

Although the omniforms app accounts for the majority of use cases you may have models that use custom model fields.  In these instances the form builder will not be able to map a model field to a form field and you will need to provide a custom field mapping using the `OMNI_FORMS_CUSTOM_FIELD_MAPPING` setting.

 - Each key within the mapping dictionary must be a string (python dotted import path) to a model field class.
 - Each value within the mapping dictionary must be a string (python dotted import path) to an OmniField subclass.

For example, you can map a TagField to an OmniCharField model instance using the following configuration:

```
OMNI_FORMS_CUSTOM_FIELD_MAPPING = {
    'taggit.TagField': 'omniforms.models.OmniCharField',
}
```

With this configuration any instances of taggit.TagField on your models will be represented as charfields in the corresponding forms generated by omniforms.

It is also possible to create your own OmniField subclasses to use in your custom form builders.  For example:

```
OMNI_FORMS_CUSTOM_FIELD_MAPPING = {
    'taggit.TagField': 'my_app.MySuperOmniField',
}
```

It is important to note that the dictionary values defined within the `OMNI_FORMS_CUSTOM_FIELD_MAPPING` MUST be subclasses of `omniforms.models.OmniField`.  If you attempt to register Field handlers that do not subclass `omniforms.models.OmniField` an ImproperlyConfigured exception will be raised.

## Compatibility

This app is compatible with the following django versions:

 - Django 1.8.x
 - Django 1.9.x
 - Django 1.10.x

## ChangeLog

 - 0.1 - Initial Build
