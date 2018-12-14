To correctly work with Anaconda on Powershell :

* Run the anaconda command : 
```bash
C:\Users\elias\Anaconda3> cmd C:\Users\elias\Anaconda3\envs\py35\Scripts\activate.bat C:\Users\elias\Anaconda3\envs\py35\Scripts\activate.bat
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.
```

* List the available environments:

```bash
conda info --envs
```

* Activate your env :
```bash
C:\Users\elias\Anaconda3>activate py35
```

* Deactivate your env : 
```bash
(py35) C:\Users\elias\Anaconda3>deactivate
```

* Close cmd to go back to the powershell prompt : 
```bash
C:\Users\elias\Anaconda3>exit
PS C:\Users\elias\Anaconda3>
```