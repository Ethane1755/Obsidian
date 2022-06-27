# Untitled 4
Interesting target.
Processed in Pixinsight and Photoshop

Pixinsight:
OSC:
1.ABE
2.ColorCalibration
3.SCNR Green 0.8

Ha:
1.ABE
2.Create TGV Mask
3.TGVDenoise

Luminance:
1.MMT
2.Create TGV Mask
3.TGVDenoise
4.STF+HT stretch
5.HT bring up black point

Combine:
1.NBRGBCombination
2.Ha as 5.00nm and scale as 1.2
3.MaskedStretch on Colored
4.CurvesTransformation on Colored
5.LRGBCombination

Photoshop:
1.Crop
2.Camera Raw Filter (Curves,Saturation,Color Noise Reduction etc.)
3.Selective Color


