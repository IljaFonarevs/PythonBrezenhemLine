An implementation of Brezenhem Alghorithm in order to draw a line and animate a circle on it. This was a task given at my university so I did not have any particular goals in mind, but it certainly given me some insights into python basics and some of its libraries such as pygame and tkinter. 
In the earlier version of the project I tried to use turtle, PyQT5 and PySimpleGui, but for the sake of simplicity I decided to switch to the pygame and tkinter

Pros:
    Simplicity: I have written this program with a very little knowledge of python, so it should be pretty simple to anyone who knows Brezenhem Alghoritm and coded something on python
    Modularity: Due to python features, the program can be easily extended
Cons:
    UI: Interface is old-looking and overall ugly
    Efficiency: Programm draws entire frame from scratch, while the only moving part on the screen is red circle, it wastes a lot of recources
Ways-To-Improve:
    Improve UI, change animation alghoritm, add curves, add ability to draw with mathematical functions, add pause, add ability to change velocity on the fly, add moving figure shape and color customisation.
