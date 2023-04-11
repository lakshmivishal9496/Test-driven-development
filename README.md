<h1 align="center">Pig (dice game)</h1>

<p align="left">
  Here you should add general information about the project
  <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [👨‍💻 Description ](#-description-)
- [🏁 Getting Started ](#-getting-started-)
    - [Installing (Dependency)](#installing dependency for project)
    - [Installing the game](#-how to install game-)
  - [Usage](#usage)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)

## 🧐 About <a name = "about"></a>

This is a general template for any Python project you want to start working on.

*Here you can add 1-2 paragraphs on information about the project*

## 👨‍💻 Description <a name = "description"></a>

*Here you can add a description for your project and its purpose*

## 🏁 Getting Started <a name = "getting_started">
<img src = "src\dice.gif">
</a>

### Installing Dependency
*These are essential tools to install before even downloading the game*

### Installing Game
*Here you can add a description on how to install the project*

### Usage

*Here you can add a description on how to run and use the project*


## ⛏️ Built Using <a name = "built_using"></a>

*Here you can link the packages/modules/dependencies used to build your project*

## ✍️ Authors <a name = "authors"></a>

*Here you can add a list of authors/people who worked and maintain the project*

- [@abshir](https://github.com/abshir112) - Idea & Initial work
- [@Lakshmi](https://github.com/lakshmivishal9496 ) - Idea & Initial work


### Check version of Python
Check what version of Python you have. The Makefile uses `PYTHON=python` as default.


<h1>Check you Python installation<h1>
make version
<p>If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.
chocolatey is the package manager/ installer which is used to install make(Note: Run Powershell as administrator and then use the command choco install make so make is installed in our computer )
To check whether we installed make succesfully and also which version of make we have
make version </p>
<h1>Python virtual environment<h1>
<p>Install a Python virtual environment and activate it.<p>
<h1>Activate on Windows</h1>
<h3>. .venv/Scripts/activate</h3>
<h1>Activate on Linx/Mac</h1>
<h3>. .venv/bin/activate</h3>
<p>When you are done you can leave the venv using the command `deactivate`.<p>
<h1>Install the dependencies</h1>

<p>
Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.
</p>
<h3 align = "center"> <b>make install-requirements</b> </h3>
<h3 align = "center"> <b>make install-toml</b> </h3>
<h1>Check what is installed</h1>
<h3 align = "center"> <b> make build-toml</b> </h3>
<h1>Execute the main program</h1>
<h3 align = "center"> <b> make run</b> </h3>
<h1>Run the validators</h1>
<p>You can run the static code validators like this. They check the sourcecode and exclude the testcode.<p>

# Run each at a time
<h3 align = "center"> <b> make flake8</b> </h3>
<h3 align = "center"> <b> make pylint</b> </h3>

<h1>Run the unittests with coverage</h1>
<h3 align = "center"> <b> make coverage</b> </h3>

<h1>Run the unittests</h1>
<h3 align = "center"> <b> make test </b> </h3>


<h1>Remove generated files</h1>
<h2>You can remove all generated files by this.</h2>
# Remove files generated for tests or caching
<h3 align = "center"> <b> make clean </b> </h3>
# Do also remove all you have installed
<h3 align = "center" > <b> make clean all </b> </h3>

<h1>Codestyle with black</h1>
You can unify the codestyle using black. Running black will change your source code to have a codestyle according to black codestyle.
<h3 align = "center"> <b> make black </b> </h3>
