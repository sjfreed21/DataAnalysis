#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 20:38:19 2020

@author: zhwa2432
"""

import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=2)
pca.fit(X)
print('\nexplained_variance_ratio\n',pca.explained_variance_ratio_)
print('\nsingular_values:\n',pca.singular_values_)
principalComponents=pca.transform(X)
print('\nprincipalComponents:\n',principalComponents)

#%%
principalComponents=pca.fit_transform(X)
print('\nprincipalComponents:\n',principalComponents)

