# fgo-auto-run

*A python + adb semi-auto script for FGO.*

## How to use it

All change parameter parts are change the `config.py` file.

And `RUN SCRIPT` \<--\> `python main.py`

Image files in `./cfg` path need to check every new task. (servant_x.png may need delete manually)

1. Change `dbg_shoot` to 1 to enable shoot DEBUG mode

    ```python
    # for debug use
    dbg_shoot = 1
    ```
    
    * Get some screenshoot which contains the part of information you need.
    
    * Then `RUN SCRIPT`
    
    * For example, `task`, `support（servant/skill/craft)`, `material` and so on.
    
    * `default_rotation` may need changed for different mobile phones.
    
2. Crop the picture you have got in step 1 to the suitable size. You can find some examples below. 

    ***Note that all images are in png format.***
    
    *task.png / material.png should be used*

    ![task](https://github.com/airbirdx/fgo-auto-run/blob/master/lib/readme/task.png)
    
    task

3. Put all the info image to the **`./cfg`** folder. (`task`, `support` ...)
   
4. If you need set the servant priority in the task, you need to do the train first.

    * Use step 1 to get some screenshoots which are in attack scene, the more servants in the scene, the better. Just lisk this.
    
        ![train_0](https://github.com/airbirdx/fgo-auto-run/blob/master/lib/readme/train_0.png)
    
    * Rename image to `train_{n}.png`, n is start from 0. And put it into **`./cfg`** folder
    
    * In order to get a precise training result, maybe more than 3 pic for this step is better.
    
    * And you can also change the order between 0/1/2 and 3/4/5 in team scene to start battle. Then do above steps again.
    
    * Change `dbg_shoot` to 1 to enable train DEBUG mode
      
        ```python
        dbg_train = 1
        ```
    * Then `RUN SCRIPT`
    
    * Find image `servant_{n}.png` in **`./cfg`** folder. And modify `servant_priority`
      
        ```python
        # servant priority, high -> low
        #                   left -> right
        servant_priority = [0, 1, 3, 2]
        ```
        
        Means servant_0 \> servant_1 \> servant_3 \> servant_2.
        
        if not use `servant_priority`, you can comment out this line by a `#` character.
    
5. Set card color priority `crd_color_priority`, just in case you want to change it. Generally, we keep it as `RGB`.

    ```python
    # R -> Blaster , high -> low
    # G -> Quick   , left -> right
    # B -> Arts
    crd_color_priority = 'RGB'
    ```
6. Config the skill and final(Baoju) if needed.

    ```python
    # skill _seq & final
    # (n) means for turn n
    # abc / ijk / opq / xyz / s
    default_skill = '(1)q(2)aijkop(3)bq31'
    # a/b/c for BaoJu(Pinyin)
    default_final = '(1)cxx(2)xxb(3)axx'
    ```
    
    `(n)` means for turn n, and it must be in the string.
    
    There is no order of the `(n)`, you can also write a `(3)q(1)aijkop` as the config.
    
    You can use space for easy read, like `(1)q(2)a ijk op(3)b q31`.

7. Config the `run_times`, `run_materials` and `run_apples` parameter. 
   
    ```python
    # How many times do you want to run
    run_times = 3
    
    
    # How many materials do you want to get
    run_materials = 3
    
    
    # How many apple do you want to eat, only support Au and Ag apple
    run_apples = ['Au', 1]
    ```
    
    * For `run_times` and `run_materials`, use apple by the order `Cu -> Ag -> Au`.
    
8. After all config, make sure you have disabled shoot and train.

    ```python
    # for debug use
    dbg_shoot = 0
    dbg_train = 0
    ```
    
    Then, `RUN_SCRIPT`.

## How to set up the environment

For python, only python3 is supported in this script.

### For Mac

use Homebrew to install python and adb.

* install homebrew
  

[homebrew](https://brew.sh/)

* install python3

```
brew install python3
```

* install adb
  
```
brew cask install android-platform-tools
```

* check adb devices

```
adb devices
```

* install adb
  
```
brew install tesseract
```

* install python lib via pip

```
pip install pillow
pip install openpyxl
pip install opencv-python
pip install numpy
pip install pytesseract
```

* install ImageMagick to less png warning during script runing

```
brew install imagemagick
```

### For Windows

* download the python3 install package and the adb dirver
* install python3
* add adb driver folder to system PATH var
* install pyhon lib (see reference for Mac)

## Note

* clean tmp info when team_confirm
* task scene, check the run_time, run_material parm.
* about run_material, only count the task number of obtained. No matter how many in one task(get 1/2/3 in one battle, all count 1).