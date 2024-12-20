{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e382a537-6bab-4450-92cd-9f07031c0b02",
   "metadata": {},
   "source": [
    "# A very simple notebook to perform some minimum install checks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d497fa4-bd1f-45f1-ad08-98c6de4f2dab",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import sys\n",
    "import platform\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "print(\"python\",sys.version)\n",
    "assert sys.version.startswith(\"3.11\")\n",
    "print(\"pandas\",pd.__version__)\n",
    "assert pd.__version__.startswith(\"2\")\n",
    "print(\"numpy\",np.version.version)\n",
    "assert np.version.version.startswith(\"1.2\")\n",
    "assert int(np.version.version.split(\".\")[1]) >= 25\n",
    "#todo: add some asserts for min versions...\n",
    "\n",
    "import flopy\n",
    "import pyemu\n",
    "assert \"dependencies\" in flopy.__file__\n",
    "assert \"dependencies\" in pyemu.__file__\n",
    "\n",
    "\n",
    "if \"linux\" in platform.platform().lower():\n",
    "    bin_dir = os.path.join(\"..\",\"bin_new\",\"linux\")\n",
    "elif \"darwin\" in platform.platform().lower() or \"macos\" in platform.platform().lower():\n",
    "    bin_dir = os.path.join(\"..\",\"bin_new\",\"mac\")\n",
    "else:\n",
    "    bin_dir = os.path.join(\"..\",\"bin_new\",\"win\")\n",
    "assert os.path.exists(bin_dir)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5cbdb869-2eca-40e7-bddc-31046265af03",
   "metadata": {},
   "outputs": [],
   "source": [
    "mat = pyemu.Matrix.from_binary(\"test.jcb\")\n",
    "plt.imshow(mat.x,cmap=\"Greys_r\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a9ac6e9c-2e03-47cb-abb0-f5c22d4e22b7",
   "metadata": {},
   "source": [
    "### If you see the 3-word pass code above, you rock! "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
