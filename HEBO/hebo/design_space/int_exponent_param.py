"""Int Exponent Param."""

# Copyright (C) 2020. Huawei Technologies Co., Ltd. All rights reserved.

# This program is free software; you can redistribute it and/or modify it under
# the terms of the MIT license.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the MIT License for more details.

import numpy as np

from .param import Parameter


class IntExponentPara(Parameter):
    """IntExponentPara."""
    
    def __init__(self, param_dict):
        """Integer value, search in log-scale, and the exponent must be integer.

        For example, parameter whose values must be one of [32, 64, 128, 512, 1024]
        """
        super().__init__(param_dict)
        self.base = param_dict['base']
        self.lb = np.round(np.log(param_dict['lb']) / np.log(self.base))
        self.ub = np.round(np.log(param_dict['ub']) / np.log(self.base))
    
    def sample(self, num=1):
        """Sample."""
        assert (num > 0)
        exponent = np.random.randint(self.lb, self.ub + 1, num)
        return self.base ** exponent
    
    def transform(self, x):
        """Transform."""
        return (np.log(x) / np.log(self.base))
    
    def inverse_transform(self, x):
        """Inverse transform."""
        return (self.base ** x).astype(int)
    
    @property
    def is_numeric(self):
        """Is Numeric."""
        return True
    
    @property
    def opt_lb(self):
        """Opt lower bound."""
        return self.lb
    
    @property
    def opt_ub(self):
        """Opt upper bound."""
        return self.ub
    
    @property
    def is_discrete(self):
        """Is discrete."""
        return True
    
    @property
    def is_discrete_after_transform(self):
        """Is discrete after trans."""
        return True
