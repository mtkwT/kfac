# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Kronecker-factored Approximate Curvature Optimizer."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint: disable=unused-import,line-too-long
from kfac.python.ops import curvature_matrix_vector_products
from kfac.python.ops import estimator
from kfac.python.ops import fisher_blocks
from kfac.python.ops import fisher_factors
from kfac.python.ops import layer_collection
from kfac.python.ops import loss_functions
from kfac.python.ops import op_queue
from kfac.python.ops import optimizer
from kfac.python.ops import utils
# pylint: enable=unused-import,line-too-long

# pylint: disable=invalid-name
LayerCollection = layer_collection.LayerCollection
KfacOptimizer = optimizer.KfacOptimizer
# pylint: enable=invalid-name
