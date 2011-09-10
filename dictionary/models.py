from django.db import models


class GeoLocationType(models.Model):
    type = models.CharField(max_length=100, blank=False)

    class Meta:
        pass

    def __unicode__(self):
        return self.type

    def to_dict(self):
        return dict(
            pk = self.pk,
            type = self.type
        )


class Dictionary(models.Model):
    name = models.CharField(max_length=100, blank=False)
    types = models.ManyToManyField(GeoLocationType)

    class Meta:
        pass

    def __unicode__(self):
        return self.name

    def to_dict(self):
        return dict(
            pk = self.pk,
            name = self.name,
            types = [type.to_dict() for type in self.types.all()]
        )

class Word(models.Model):
    name = models.CharField(max_length=255, blank=False)
    main_translation = models.CharField(max_length=255, blank=False)
    other_translations = models.TextField(blank=True)
    dictionary = models.ForeignKey(Dictionary)

    class Meta:
        pass

    def __unicode__(self):
        return self.name

    def to_dict(self):
        return dict(
            pk = self.pk,
            name = self.name,
            main_translation = self.main_translation,
            other_translations = self.other_translations,
        )
