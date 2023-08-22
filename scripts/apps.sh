#!/bin/bash

var1="Apple" #global variable
myfun(){
    local var2="Banana" #local variable
    var3="Cherry" #global variable
    echo "The name of first fruit is $var1"
    echo "The name of second fruit is $var2"
}
myfun #calling function