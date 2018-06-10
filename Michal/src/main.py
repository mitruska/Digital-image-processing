from unification import Unification
from histogram_gray import HistogramGray
from histogram_color import HistogramColor
from filter import Filter
from PIL import Image, ImageFilter
import  numpy as np
import math
import colorsys

zad1 = "img/zad1/"
zad5 = "img/zad5/"
zad6 = "img/zad6/"
zad9 = "img/zad9/"

#im = Image.open(zad9 + "HSI_filtr_kompasowy_Sobol_(2).png")
#im.save(zad9 + "HSI_filtr_kompasowy_Sobol_(2).tiff")




ex1 = Unification(zad1 + "pirate_gray.tiff", zad1 + "gentelman_gray.tiff")
#ex1.geometricGray(show=False)
#ex1.rasterGray(show=False)
ex1.load(zad1 + "peppers_color.tiff", zad1 + "lena_color.tiff")
#ex1.geometricColor(show=False)
#ex1.rasterColor(show=False)
##
ex5 = HistogramGray(zad5 + "gentelman_gray.tiff")
#ex5.calculate(plot=True, image=None)
#ex5.move(const=100, show=False, plot=True)
#ex5.stretch(show=True, plot=True)
#ex5.localThreshold(dim=20, show=False, plot=True)
#ex5.globalThreshold(show=False, plot=True)
ex5.load(zad5 + "pirate_gray.tiff")
#ex5.calculate(plot=True, image=None)
#ex5.move(const=-100, show=False, plot=True)
#ex5.stretch(show=False, plot=True)
#ex5.localThreshold(dim=20, show=False, plot=True)
#ex5.globalThreshold(show=False, plot=True)
##
ex6 = HistogramColor(zad6 + "lena_color.tiff")
#ex6.calculate(plot=True)
#ex6.move(50, show=False, plot=True)
#ex6.stretch(show=False, plot=True)
#ex6.monoThresholding(show=False, plot=False)
#ex6.globalSingleThreshold(show=False, plot=True)
#ex6.globalMultiThreshold(bins=4, show=False, plot=True)
#ex6.localSingleThreshold(dim=21, show=False, plot=True)
#ex6.localMultiThreshold(dim=21, bins=4, show=False, plot=True)
ex6.load(zad6 + "peppers_color.tiff")
#ex6.calculate(plot=True)
#ex6.move(-50, show=False, plot=True)
#ex6.stretch(show=False, plot=True)
#ex6.monoThresholding(show=False, plot=False)
#ex6.globalSingleThreshold(show=False, plot=True)
#ex6.globalMultiThreshold(bins=4, show=False, plot=True)
#ex6.localSingleThreshold(dim=21, show=False, plot=True)
#ex6.localMultiThreshold(dim=21, bins=4, show=False, plot=True)
#
ex9 = Filter(zad9 + "gentelman_gray.tiff")
#ex9.averageGray(show=False)
#ex9.gaussGray(show=False)
#ex9.robertsGray(show=False)
#ex9.prewittGray(show=False)
#ex9.sobolGray(show=False)
#ex9.compassGray(show=False)
#ex9.reliefGray(show=False)
#ex9.VDGGray(show=True)
#ex9.medianGray(show=False)
#ex9.maxGray(show=False)
#ex9.minGray(show=False)
ex9.load(zad9 + "pirate_gray.tiff")
#ex9.averageGray(show=False)
#ex9.gaussGray(show=False)
#ex9.robertsGray(show=False)
#ex9.prewittGray(show=False)
#ex9.sobolGray(show=False)
#ex9.compassGray(show=False)
#ex9.reliefGray(show=False)
#ex9.VDGGray(show=False)
#ex9.medianGray(show=False)
#ex9.maxGray(show=False)
#ex9.minGray(show=False)
ex9.load(zad9 + "lena_color.tiff")
#ex9.averageColor(show=False)
#ex9.gaussColor(show=False)
#ex9.robertsColor(show=False)
#ex9.prewittColor(show=False)
#ex9.sobolColor(show=False)
#ex9.compassColor(show=False)
#ex9.reliefColor(show=False)
#ex9.VDGColor(show=False)
#ex9.medianColor(show=False)
#ex9.maxColor(show=False)
#ex9.minColor(show=False)
ex9.load(zad9 + "peppers_color.tiff")
#ex9.averageColor(show=False)
#ex9.gaussColor(show=False)
#ex9.robertsColor(show=False)
#ex9.prewittColor(show=False)
#ex9.sobolColor(show=False)
#ex9.compassColor(show=False)
#ex9.reliefColor(show=False)
#ex9.VDGColor(show=False)
#ex9.medianColor(show=False)
#ex9.maxColor(show=False)
#ex9.minColor(show=False)

