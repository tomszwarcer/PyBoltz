# PyBoltz
This software package is a translation of the Fortran based Magboltz code (Biagi, 2001) into Cython. This project was built to allow for more productive work to be done with magboltz.

## General information.

### About PyBoltz ###

PyBoltz is an electron swarm Monte Carlo package for calculating transport parameters of electrons in different gas mixtures that are relevant to particle detectors.

To cite PyBoltz, and for more information:

```
Electron transport in gaseous detectors with a Python-based Monte Carlo simulation code
B. Al Atoum et al, Comp Phys Comm 254 (2020) 107357
https://www.sciencedirect.com/science/article/abs/pii/S0010465520301533
```

### About Magboltz.
The Magboltz program computes drift gas properties by "numerically integrating the Boltzmann transport equation"-- i.e., simulating an electron bouncing around inside a gas. By tracking how far the virtual electron propagates, the program can compute the drift velocity. By including a magnetic field, the program can also calculate the Lorentz angle. [Read more](http://cyclo.mit.edu/drift/www/aboutMagboltz.html).

### Why Cython?
Cython's static typing improves the speed of python code by about a hundred times. In other words, Cython provides us with the simplicity of python and the speed of Fortran/C. [Read more](https://cython.org/).

## Installing PyBoltz

- There are probably better ways of doing this but this is the first way I found that worked and was reproducible.

### Requirements

- This has only been reliably achieved/tested on Python 3.9.18.
- Requires `numpy 1.22.0`, `Cython 0.29.37` `setuptools` and `build`. The first three should be handled automatically by the installation process, but you should install them separately anyway as they are installed in a virtual environment which is only used in the installation process.

### Procedure

#### 1. Install `numpy 1.22.0`, `Cython 0.29.37` `setuptools` and `build`

```
$ python3 -m pip install numpy==1.22.0
$ python3 -m pip install Cython==0.29.37
$ python3 -m pip install setuptools
$ python3 -m pip install build
```

- You may need to add `--user` to the end of these commands if installing on a shared system (this was needed to install locally on the Linux machine)

#### 2. Clone PyGasMix and PyBoltz from Github

```
$ git clone git@github.com:tomszwarcer/PyGasMix.git
$ git clone git@github.com:tomszwarcer/PyBoltz.git
``` 

#### 3. Install PyGasMix

- From within your PyGasMix directory, run

```
$ python3 -m build
$ python3 -m pip install .
```

#### 4. Install PyBoltz

- From within your PyBoltz directory, open `pyproject.toml`.
- Under `[build-system]` change the path to PyGasMix to match the location of your PyGasMix directory (I will make a script that does this automatically in future). Save the file.
- Run the following:

```
$ python3 -m build
$ python3 -m pip install .
```

#### 5. Test

```
$ python3 examples/Example.py 
```
### Running PyBoltz.
To run the code, you will need to import PyBoltz and instantiate an instance of the PyBoltz object, fill in the input parameters and call the PyBoltz.Start() function. There are examples in the Examples directory on to how to use PyBoltz. The main example is the Test_PyBoltz_NoWrapper.py code. This example also has a list of the gases in PyBoltz.

#### Input parameters.
* **PyBoltz.NumberOfGases** - The number of gases in the mixture (goes up to 6).
* **PyBoltz.MaxNumberOfCollisions** - The number of simulated events / 2*10E7.
* **PyBoltz.Enable_Penning** - Penning effects included (0 or 1).
* **PyBoltz.Enable_Thermal_Motion** - Thermal motion included (0 or 1).
* **PyBoltz.Max_Electron_Energy** - Upper limit of electron energy integration (0.0 to automatically calculate this value).
* **PyBoltz.GasIDs** - Array of six elements that has the number of each gas in the mixture.
* **PyBoltz.GasFractions** - Array of six elements that has the percentage of each gas in the mixture.
* **PyBoltz.TemperatureCentigrade** - The tempreture in degrees centigrade.
* **PyBoltz.Pressure_Torr** - The pressure \[torr\].
* **PyBoltz.EField** - The electric field in the chamber \[Volts/Cm\].
* **PyBoltz.BField_Mag** - The magnitude of the magentic field \[KiloGauss\].
* **PyBoltz.BField_Angle** - The angle between the magentic field and the electric field. 
* **PyBoltz.Which_Angular_Model** - This variable is used to fix the angular distrubtions to one of the following types. 
  - Okhrimvoskky Type - PyBoltz.WhichAngularModel = 2 (default value).
  - Capitelli Longo Type - PyBoltz.WhichAngularModel = 1.
  - Isotropic Scattering - PyBoltz.WhichAngularModel = 0.
* **PyBoltz.Console_Output_Flag** - This variable is used to tell PyBoltz to print to the console.
  - Print to the console - PyBoltz.ConsoleOutputFlag = 1.
  - Avoid printing to the console - PyBoltz.ConsoleOutputFlag = 0.
* **PyBoltz.Random_Seed** - This variable is used to set the seed for the random number geenerator used by the simulation. 

#### Output parameters.
Please note that the following are only the main output parameters. One can still get any value from the parameters within the Magboltz class.

* **PyBoltz.VelocityZ** - Drift velocity in the Z direction \[mm/mus\].
* **PyBoltz.VelocityY** - Drift velocity in the Y direction \[mm/mus\].
* **PyBoltz.VelocityX** - Drift velocity in the X direction \[mm/mus\].
* **PyBoltz.VelocityErrorZ** - Error for the Magboltz.WZ value (+- Magboltz.DWZ * Magboltz.WZ).
* **PyBoltz.VelocityErrorY** - Error for the Magboltz.WY value (+- Magboltz.DWY * Magboltz.WY).
* **PyBoltz.VelocityErrorX** - Error for the Magboltz.WX value (+- Magboltz.DWX * Magboltz.WX).
* **PyBoltz.TransverseDiffusion** - Transverse diffusion \[cm^2/s\].
* **PyBoltz.TransverseDiffusionError** - Error for the Magboltz.DIFTR value (+- Magboltz.DFTER * Magboltz.DIFTR).
* **PyBoltz.LongitudinalDiffusion** - Longitudinal diffusion \[cm^2/s\]..
* **PyBoltz.LongitudinalDiffusionError** - Error for the Magboltz.DIFLN value (+- Magboltz.DFLER * Magboltz.DIFLN).
* **PyBoltz.TransverseDiffusion1** - Transverse diffusion \[mum/cm^0.5\].
* **PyBoltz.TransverseDiffusion1Error** - Error for the Magboltz.DTMN value (+- Magboltz.DTMN * Magboltz.DFTER1).
* **PyBoltz.LongitudinalDiffusion1** - Longitudinal diffusion \[mum/cm^0.5\].
* **PyBoltz.LongitudinalDiffusion1Error** - Error for the Magboltz.DLMN vlaue (+- Magboltz.DLMN * Magboltz.DFLER1).
* **PyBoltz.MeanElectronEnergy** - Mean electron energy \[eV\].
* **PyBoltz.MeanElectronEnergyError** - Error for the Magboltz.AVE value (+- Magboltz.AVE * Magboltz.DEN).
* **PyBoltz.DiffusionX** - Diffusion in the X plane \[cm^2/s\].
* **PyBoltz.ErrorDiffusionX** - Error for the Magboltz.DIFXX value (+- Magboltz.DIFXX * Magboltz.DXXER).
* **PyBoltz.DiffusionY** - Diffusion in the Y plane \[cm^2/s\].
* **PyBoltz.ErrorDiffusionY** - Error for the Magboltz.DIFYY value (+- Magboltz.DIFYY * Magboltz.DYYER).
* **PyBoltz.DiffusionZ** - Diffusion in the Z plane \[cm^2/s\].
* **PyBoltz.ErrorDiffusionZ** - Error for the Magboltz.DIFZZ value (+- Magboltz.DIFZZ * Magboltz.DZZER).
* **PyBoltz.DiffusionYZ** - Diffusion in the YZ plane \[cm^2/s\].
* **PyBoltz.ErrorDiffusionYZ** - Error for the Magboltz.DIFYZ value (+- Magboltz.DIFYZ * Magboltz.DYZER).
* **PyBoltz.DiffusionXY** - Diffusion in the XY plane \[cm^2/s\].
* **PyBoltz.ErrorDiffusionXY** - Error for the Magboltz.DIFXY value (+- Magboltz.DIFXY * Magboltz.DXYER).
* **PyBoltz.DiffusionXZ** - Diffusion in the XZ plane \[cm^2/s\].
* **PyBoltz.ErrorDiffusionXZ** - Error for the Magboltz.DIFXZ value (+- Magboltz.DIFXZ * Magboltz.DXZER).
* **PyBoltz.MeanCollisionTime** - Mean Collision Time.
* **TOF Outputs** - Those outputs include townsend coeffiecents, diffusion and energy values. Those outputs are calculated from the time of flight simulation. Check the PyBoltz object documentation for more details.
* **SST Outputs** - Those outputs include townsend coeffiecents, diffusion and energy values. Those outputs are calculated from the steady state simulation. Check the PyBoltz object documentation for more details.
* **Collision type counters** - Six elements arraies that houses the number of collisions of each gas for each types. The types are elastic, inelastic, super-elastic, ionisation, and attachment. Check the PyBoltz object documentaion for more details.

#### Compilation issues.
This sections is written here to help troubleshoot compilation issues. The following are links to the two main issues:

* [First Issue](https://github.com/UTA-REST/PyBoltz/issues/1).
* [Second Issue](https://github.com/UTA-REST/PyBoltz/issues/2).

## Gas list.
The current PyBoltz version has the following gases. Please note that the number of the gas is used as an indicator to that gas in the code. 

* **CF4** - Gas # 1.
* **Argon** Gas # 2.
* **Helium-4** Gas # 3.
* **Helium-3** Gas # 4.
* **Neon** Gas # 5.
* **Krypton** Gas #6.
* **Xenon** Gas # 7.
* **CH4** Gas # 8.
* **Ethane** Gas # 9.
* **Propane** Gas # 10.
* **Isobutane** Gas # 11.
* **CO2** Gas # 12.
* **H2O** Gas # 14.
* **Oxygen** Gas # 15.
* **Nitrogen** Gas # 16.
* **Hydrogen** Gas # 21.
* **Deuterium** Gas # 22.
* **DME** Gas # 25.
* **XenonMert** Gas # 61 (This gas requires extra parameters, check /Examples/Test_PyBoltz_mert.py).


## Documentation link
[Documentation...](https://uta-rest.github.io/PyBoltz-Documentation/html/).
