============
Quick Start
============

DeepOBS is a Python package to benchmark deep learning optimizers. It currently supports TensorFlow.

We tested the package with Python 2.7 and TensorFlow version 1.10. Other versions of Python and TensorFlow (>= 1.4.0) might work, and we plan to expand compatibility in the future.

Installation
==============

You can install the latest stable release of DeepOBS using `pip`:

.. code-block:: bash

   pip install git+https://github.com/anonymousICLR2019submitter/DeepOBS.git

.. NOTE::
  The package requires the following packages:

  - argparse
  - importlib
  - numpy
  - seaborn
  - matplotlib2tikz
  - pandas

  TensorFlow is not a required package to allow for both the CPU and GPU version. Make sure that one of those is installed.

.. HINT::
  We do not specify the exact version of the required package. However, if any problems occur while using DeepOBS, it might be a good idea to upgrade those packages to the newest release (especially matplotlib and numpy).

Set-Up Data Sets
================

After installing DeepOBS, you have to download the data sets for the test problems. This can be done by simply running

.. code-block:: bash

  deepobs_prepare_data.sh

This will automatically download, sort and prepare all the datasets (except ImageNet) in a folder called ``data_deepobs`` in the current directory. It can take a while, as it will download roughly 1 GB.

.. NOTE::
  The ImageNet data set is currently excluded from this automatic downloading and preprocessing. ImageNet requires a registration to do this and has a total size of hundreds of GBs. You can download it and add it to the imagenet folder by yourself if you wish to use the ImageNet data set.

.. HINT::
  If you already have some of the data sets on your computer, you can only download the rest. If you have all data sets, you can skip this step, and always tell DeepOBS where the data sets are located. However, the DeepOBS package requires the data sets to be organized in a specific way.

You are now ready to run different optimizers on different test problems, you can try for example

.. code-block:: bash

  deepobs_run_sgd.py mnist.mnist_mlp --num_epochs=2 --lr=1e-1 --bs=128 --nologs

to run SGD on a simple multi-layer perceptron (with a learning rate of 1e-1 and a batch size of 128 for 4 epochs without keeping logs).

Contributing to DeepOBS
=======================

We invite the authors of other algorithms to add their own method to the benchmark. Just edit a run script to include the new optimization method and create a pull-request.

Provided that this new optimizer produces competitive results, we will add the results to the set of provided baselines.
