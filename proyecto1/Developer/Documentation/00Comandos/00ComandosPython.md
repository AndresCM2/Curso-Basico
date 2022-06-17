# Comandos Python

### Crear entorno remoto
```
py -m venv <Nombre de la carpeta>
```
### Crear entorno virtual en virtual en
```
virtalenv venv
```
En caso se requerir un entorno virtual con una versión de python en especifico ingresar el siguiente comando
```
virtalenv venv --python=python3.7
```
### Abrir entorno virtual 
Entorno de Linux
```
source venv/bin/activate
``` 
Entorno de windows

```cmd
.\venv\Scripts\activate
```
### Salir del entorno virtual
```
deactivate
```
### Ver que modulos tenemos instalados
```
pip freeze
```
### Comando para instalar modulos
```
pip install <nombre del modulo>
```
```
pip install <nombre del modulo>
```
hay diferentes  mudulos importantes como  lo son 

-[Pandas](https://pandas.pydata.org/)

### Instalar Flask
```
pip install flak
```


#### Guardar archivo de las dependencias instaladas
```
pip freeze > requirements.txt
```
### Instalar las dependencias en otro equipo
```
pip install -r riquirements.txt
```
> Nota: PYENV es la maquina virtual por defecto que tiene python pero exiten otras como son PIPENV

### Instalacion de virtualenv En windows

```
pip install virtualenv
```
### Instalacion de virtualenv en MAC  
```
pip easy_install pip
```
### Instalacion de virtualenv manera global CORE  
```
pip install virtualenv
```
### Habilitar Scritp Cuando aparece el siguiente error

```
Set-ExecutionPolicy : No se encuentra ningún parámetro que coincida con el nombre del parámetro 'List'.
En línea: 1 Carácter: 21
+ Set-ExecutionPolicy -List
+                     ~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Set-ExecutionPolicy], ParameterBindingException
    + FullyQualifiedErrorId : NamedParameterNotFound,Microsoft.PowerShell.Commands.SetExecutionPolicyCommand
```
```
Get-ExecutionPolicy -list
```
Al ejecutar este comando aparece la siguiente linea
```
  Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser       Undefined
 LocalMachine       Undefined

```
Si ejecutamos el siguiente comando se habilitara LocalMachine
```
Set-ExecutionPolicy RemoteSigned -Force
```
```
Get-ExecutionPolicy -list+
```
Al ejecutar este comando aparece la siguiente linea
```
  Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser       Undefined
 LocalMachine       RemoteSigned

```
Posterior a esto tenemos que habilitar El ```MachinePolicy``` oprimiento del comando Ctrl + r y ejecuntamos el siguiente codigo gpedit.msc 
y en la siguiente ruta habilitar los scripts

> Plantillas administrativas / Componentes de Windows / Windows PowerShell / ---> le damos la la opción. Activar la ejecución de Scripts  ----> a Esto le damos habilitar y permitir solo scripts firmados

De esta forma ejecutamos nuevamente el comando para ingresar a al entorno virtual



