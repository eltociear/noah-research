# Copyright (C) 2020. Huawei Technologies Co., Ltd. All rights reserved.

# This program is free software; you can redistribute it and/or modify it under
# the terms of the MIT license.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the MIT License for more details.

"""Extending mindspore with some util functions."""

import mindspore as ms
import mindspore.numpy as mnp
import numpy as np
from mindspore import Tensor, ops


def randn(*np_args) -> Tensor:
    """Generate a random number in mindspore tensor."""
    return Tensor(np.random.randn(*np_args), ms.float32)


def ones(shape) -> Tensor:
    """Usage x = ones((3, 4))."""
    return mnp.ones(shape)


def zeros(shape) -> Tensor:
    """Generate tensor of zeros of size shape."""
    # NOTE: `ops.Zeros` does not support creating tensor of shape `(N, 0)`
    return mnp.zeros(shape)
    # return ms.ops.Zeros()(shape, ms.float32)


def sum(x: Tensor, axis=(), keep_dims=False):
    """Sum mindspore tensor."""
    func = ops.ReduceSum(keep_dims=keep_dims)
    return func(x, axis=axis)


def from_numpy(x: np.array, dtype=None) -> Tensor:
    """Convert numpy to mindspore tensor."""
    if 0 not in x.shape:
        return Tensor(x, dtype=dtype)
    else:
        return mnp.zeros(x.shape)


sqrt = ops.Sqrt()
isfinite = ops.IsFinite()
