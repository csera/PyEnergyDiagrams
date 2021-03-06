# PyEnergyDiagrams
This is a simple script to plot energy profile diagrams using Python and matplotlib.
Fork of giocomomarchioro's original version (commit c9434060cd3c2e0f3455e3131464fa93daff8c14)

![alt tag](https://github.com/giacomomarchioro/PyEnergyDiagrams/blob/master/md_images/Final.png)
## Requirments
  > [matplotlib](http://matplotlib.org/users/installing.html)
  
## How to use it?

Put your script in your Python path.

```python
from energydiagram import ED
diagram = ED()
diagram.add_level(0,'Separated Reactants')
diagram.add_level(-5.4,'mlC1')
diagram.add_level(-15.6,'mlC2','last',) # 'last' places this in the same col as the immediately preceding level
diagram.add_level(28.5,'mTS1',color='g')
diagram.add_level(-9.7,'mCARB1')
diagram.add_level(-19.8,'mCARB2','last')
diagram.add_level(20,'mCARBX','last')
```

Set your y axis label:

```python
diagram.set_yName("Energy \ $kcal mol^(-1)$")
```
Note that you can pass LaTeX expressions in with the label string.

Show the IDs (red numbers) to understand how to link the levels:

```python
diagram.plot(show_IDs=True) #show_IDs is optional and is False by default
```
![alt tag](https://github.com/giacomomarchioro/PyEnergyDiagrams/blob/master/With_IDs.png)

Add the links using `diagram.add_link(starting_level_ID,ending_level_ID)`:
```python
diagram.add_link(0,1)
diagram.add_link(0,2)
diagram.add_link(2,3)
diagram.add_link(1,3)
diagram.add_link(3,4)
diagram.add_link(3,5)
diagram.add_link(0,6)
```

Plot the final result:
```python
diagram.plot()
```
The results are displayed above.

## Trouble shooting and fine tuning
Insufficient energy level padding can cause display issues. You can adjust this as below:
```python
diagram.offset = 10
```
![alt tag](https://github.com/giacomomarchioro/PyEnergyDiagrams/blob/master/md_images/Explained.jpg)

If you don't see anything try:
```python
import matplotlib.pyplot as plt
plt.show()
```
