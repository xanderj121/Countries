# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 20:54:10 2023

@author: xande
"""

import numpy as np
pscd = np.array ([108, 110, 112, 114, 109, 100, 113, 120, 120])
tscd = np.array ([103, 108, 106, 95, 103, 98, 115, 110, 109])
kscd = np.array([82, 62, 68, 90, 92, 95, 87, 107, 91])

print('Mean, Median \n Stop Closure Duration \n p',
      np.mean(pscd),
      np.median(pscd),
      '\n t',
      np.mean(tscd),
      np.median(tscd),
      '\n k',
      np.mean(kscd),
      np.median(kscd)
      )


pvot = np.array([85, 87, 98, 90, 80, 94, 86, 78, 62])
tvot = np.array([99, 101, 84, 80, 122, 112, 94, 89, 97])
kvot = np.array([114, 121, 128, 126, 127, 127, 121, 118, 123])

print('Mean, Median \n Voice Onset Time \n p',
      np.mean(pvot),
      np.median(pvot),
      '\n t',
      np.mean(tvot),
      np.median(tvot),
      '\n k',
      np.mean(kvot),
      np.median(kvot)
      )
