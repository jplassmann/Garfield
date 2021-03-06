# coding: utf-8
###
 # @file   averaged-median.py
 # @author Sébastien Rouault <sebastien.rouault@alumni.epfl.ch>
 #
 # @section LICENSE
 #
 # Copyright © 2018-2019 École Polytechnique Fédérale de Lausanne (EPFL).
 # See LICENSE file.
 #
 # @section DESCRIPTION
 #
 # Synchronous averaged-median with support for NaN coordinates GAR.
###

import tensorflow as tf

from . import _GAR, register

# ---------------------------------------------------------------------------- #
# Average with support for NaN coordinates GAR class

class AveragedMedianGAR(_GAR):
  """ Synchronous averaged-median with support for NaN coordinates GAR class.
  """

  def __init__(self, nbworkers, nbbyzwrks, args):
    self.__beta = nbworkers - nbbyzwrks

  def aggregate(self, gradients):
    # Assertion
    assert len(gradients) > 0, "Empty list of gradient to aggregate"
    # Computation
    gradients = tf.parallel_stack(gradients)
    return tf.py_func(self._aggregate, [gradients], gradients.dtype, stateful=False, name="GAR_averaged-median")

# ---------------------------------------------------------------------------- #
# GAR registering

# Register aggregation rule
register("averaged-median", AveragedMedianGAR)
