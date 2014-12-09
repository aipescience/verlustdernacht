from __future__ import unicode_literals

from django.db import models

class AnaBabelsberg(models.Model):
    mjd = models.IntegerField(primary_key=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    dev_mags = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ana_babelsberg'

class AnaBbergSave(models.Model):
    mjd = models.IntegerField(primary_key=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ana_bberg_save'

class AnaDahlem(models.Model):
    mjd = models.IntegerField(primary_key=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    dev_mags = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'ana_dahlem'

class AnaDahlem2(models.Model):
    mjd = models.IntegerField(primary_key=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    dev_mags = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ana_dahlem_2'

class AnaDahlem2Old(models.Model):
    mjd = models.IntegerField(blank=True, null=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ana_dahlem_2_old'

class AnaDahlem4Filterless(models.Model):
    mjd = models.IntegerField(primary_key=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    dev_mags = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ana_dahlem_4_filterless'

class AnaDahlem5Red(models.Model):
    mjd = models.IntegerField(primary_key=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    dev_mags = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ana_dahlem_5_red'

class AnaDahlem6Green(models.Model):
    mjd = models.IntegerField(primary_key=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    dev_mags = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ana_dahlem_6_green'

class AnaDahlem7Blue(models.Model):
    mjd = models.IntegerField(primary_key=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    dev_mags = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ana_dahlem_7_blue'

class AnaDahlemOld(models.Model):
    mjd = models.IntegerField(blank=True, null=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    dev_mags = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'ana_dahlem_old'

class AnaFreienbrink(models.Model):
    mjd = models.IntegerField(primary_key=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ana_freienbrink'

class AnaFriedrichshagen(models.Model):
    mjd = models.IntegerField(primary_key=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ana_friedrichshagen'

class AnaObservatorioDelTeide(models.Model):
    mjd = models.IntegerField(primary_key=True)
    start_night = models.FloatField(blank=True, null=True)
    end_night = models.FloatField(blank=True, null=True)
    moon_rise = models.FloatField(blank=True, null=True)
    moon_set = models.FloatField(blank=True, null=True)
    min_mag = models.FloatField(blank=True, null=True)
    max_mag = models.FloatField(blank=True, null=True)
    mean_mag = models.FloatField(blank=True, null=True)
    dev_mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    min_mag_nomoon = models.FloatField(blank=True, null=True)
    max_mag_nomoon = models.FloatField(blank=True, null=True)
    mean_mag_nomoon = models.FloatField(blank=True, null=True)
    dev_mag_nomoon = models.FloatField(blank=True, null=True)
    moonfree = models.FloatField(blank=True, null=True)
    phase_moon_rise = models.FloatField(blank=True, null=True)
    phase_moon_set = models.FloatField(blank=True, null=True)
    ill_moon_rise = models.FloatField(blank=True, null=True)
    ill_moon_set = models.FloatField(blank=True, null=True)
    ndat = models.IntegerField(blank=True, null=True)
    ndat_dark = models.IntegerField(blank=True, null=True)
    ndat_nomoon = models.IntegerField(blank=True, null=True)
    mags = models.TextField(blank=True) # This field type is a guess.
    mjds = models.TextField(blank=True) # This field type is a guess.
    dev_mags = models.TextField(blank=True) # This field type is a guess.
    temps = models.TextField(blank=True) # This field type is a guess.
    clear_fraction = models.FloatField(blank=True, null=True)
    ndat_noclouds = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ana_observatorio_del_teide'

class MarkproBabelsberg2(models.Model):
    mjd = models.FloatField(primary_key=True)
    cts = models.IntegerField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    flag1 = models.IntegerField(blank=True, null=True)
    flag2 = models.IntegerField(blank=True, null=True)
    ok = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'markpro_babelsberg2'

class MarkproBerlinFriedrichshain(models.Model):
    mjd = models.FloatField(primary_key=True)
    cts = models.IntegerField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    flag1 = models.IntegerField(blank=True, null=True)
    flag2 = models.IntegerField(blank=True, null=True)
    ok = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'markpro_berlin_friedrichshain'

class MarkproBerlinSpandau(models.Model):
    mjd = models.FloatField(primary_key=True)
    cts = models.IntegerField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    flag1 = models.IntegerField(blank=True, null=True)
    flag2 = models.IntegerField(blank=True, null=True)
    ok = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'markpro_berlin_spandau'

class MarkproBerlinTreptow(models.Model):
    mjd = models.FloatField(primary_key=True)
    cts = models.IntegerField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    flag1 = models.IntegerField(blank=True, null=True)
    flag2 = models.IntegerField(blank=True, null=True)
    ok = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'markpro_berlin_treptow'

class Nutzung(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    query = models.CharField(max_length=255, blank=True)
    agent = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'nutzung'

class SaveLocations(models.Model):
    serial_number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    name_short = models.CharField(max_length=255, blank=True)
    device = models.CharField(max_length=255, blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    protocol_version = models.IntegerField(blank=True, null=True)
    feature_version = models.IntegerField(blank=True, null=True)
    model_number = models.IntegerField(blank=True, null=True)
    light_calibration_offset = models.FloatField(blank=True, null=True)
    dark_calibration_time = models.FloatField(blank=True, null=True)
    calibration_offset = models.FloatField(blank=True, null=True)
    mag_cloud = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'save_locations'

class SqmBabelsberg(models.Model):
    mjd = models.FloatField(primary_key=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    exp = models.IntegerField(blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    counts = models.IntegerField(blank=True, null=True)
    period = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_babelsberg'

class SqmBabelsberg3(models.Model):
    mjd = models.FloatField(primary_key=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    exp = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_babelsberg3'

class SqmDahlem(models.Model):
    mjd = models.FloatField(primary_key=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_dahlem'

class SqmDahlem2(models.Model):
    mjd = models.FloatField(primary_key=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_dahlem_2'

class SqmDahlem2Old(models.Model):
    mjd = models.FloatField(blank=True, null=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_dahlem_2_old'

class SqmDahlem2Save(models.Model):
    mjd = models.FloatField(blank=True, null=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_dahlem_2_save'

class SqmDahlem3(models.Model):
    mjd = models.FloatField(primary_key=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_dahlem_3'

class SqmDahlem4Filterless(models.Model):
    mjd = models.FloatField(primary_key=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_dahlem_4_filterless'

class SqmDahlem5Red(models.Model):
    mjd = models.FloatField(primary_key=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_dahlem_5_red'

class SqmDahlem6Green(models.Model):
    mjd = models.FloatField(primary_key=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_dahlem_6_green'

class SqmDahlem7Blue(models.Model):
    mjd = models.FloatField(primary_key=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_dahlem_7_blue'

class SqmDahlemOld(models.Model):
    mjd = models.FloatField(blank=True, null=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_dahlem_old'

class SqmDahlemSave(models.Model):
    mjd = models.FloatField(blank=True, null=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_dahlem_save'

class SqmFreienbrink(models.Model):
    mjd = models.FloatField(primary_key=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_freienbrink'

class SqmFriedrichshagen(models.Model):
    mjd = models.FloatField(primary_key=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_friedrichshagen'

class SqmLocations(models.Model):
    serial_number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    name_short = models.CharField(max_length=255, blank=True)
    device = models.CharField(max_length=255, blank=True)
    version = models.CharField(max_length=255, blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    protocol_version = models.IntegerField(blank=True, null=True)
    feature_version = models.IntegerField(blank=True, null=True)
    model_number = models.IntegerField(blank=True, null=True)
    light_calibration_offset = models.FloatField(blank=True, null=True)
    dark_calibration_time = models.FloatField(blank=True, null=True)
    calibration_offset = models.FloatField(blank=True, null=True)
    operate_from = models.DateTimeField(blank=True, null=True)
    operate_until = models.DateTimeField(blank=True, null=True)
    key = models.CharField(max_length=255, blank=True)
    calib_a = models.FloatField(blank=True, null=True)
    calib_b = models.FloatField(blank=True, null=True)
    calib_c = models.FloatField(blank=True, null=True)
    calib_d = models.FloatField(blank=True, null=True)
    mag_cloud = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_locations'

class SqmLocationsDev(models.Model):
    serial_number = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    name_short = models.CharField(max_length=255, blank=True)
    device = models.CharField(max_length=255, blank=True)
    version = models.CharField(max_length=255, blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    protocol_version = models.IntegerField(blank=True, null=True)
    feature_version = models.IntegerField(blank=True, null=True)
    model_number = models.IntegerField(blank=True, null=True)
    light_calibration_offset = models.FloatField(blank=True, null=True)
    dark_calibration_time = models.FloatField(blank=True, null=True)
    calibration_offset = models.FloatField(blank=True, null=True)
    operate_from = models.DateTimeField(blank=True, null=True)
    operate_until = models.DateTimeField(blank=True, null=True)
    key = models.CharField(max_length=255, blank=True)
    calib_a = models.FloatField(blank=True, null=True)
    calib_b = models.FloatField(blank=True, null=True)
    calib_c = models.FloatField(blank=True, null=True)
    calib_d = models.FloatField(blank=True, null=True)
    mag_cloud = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_locations_dev'

class SqmLocationsDev2(models.Model):
    serial_number = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    name_short = models.CharField(max_length=255, blank=True)
    device = models.CharField(max_length=255, blank=True)
    version = models.CharField(max_length=255, blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    protocol_version = models.IntegerField(blank=True, null=True)
    feature_version = models.IntegerField(blank=True, null=True)
    model_number = models.IntegerField(blank=True, null=True)
    light_calibration_offset = models.FloatField(blank=True, null=True)
    dark_calibration_time = models.FloatField(blank=True, null=True)
    calibration_offset = models.FloatField(blank=True, null=True)
    operate_from = models.DateTimeField(blank=True, null=True)
    operate_until = models.DateTimeField(blank=True, null=True)
    key = models.CharField(max_length=255, blank=True)
    calib_a = models.FloatField(blank=True, null=True)
    calib_b = models.FloatField(blank=True, null=True)
    calib_c = models.FloatField(blank=True, null=True)
    calib_d = models.FloatField(blank=True, null=True)
    mag_cloud = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_locations_dev2'

class SqmLocationsSave2(models.Model):
    serial_number = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255, blank=True)
    name_short = models.CharField(unique=True, max_length=255, blank=True)
    device = models.CharField(max_length=255, blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    protocol_version = models.IntegerField(blank=True, null=True)
    feature_version = models.IntegerField(blank=True, null=True)
    model_number = models.IntegerField(blank=True, null=True)
    light_calibration_offset = models.FloatField(blank=True, null=True)
    dark_calibration_time = models.FloatField(blank=True, null=True)
    calibration_offset = models.FloatField(blank=True, null=True)
    mag_cloud = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_locations_save2'

class SqmObservatorioDelTeide(models.Model):
    mjd = models.FloatField(primary_key=True)
    mag = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    exp = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sqm_observatorio_del_teide'

