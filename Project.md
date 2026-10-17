# Retail Pipeline Project

## What does this project do?
This program is able to read sales record from a csv file, removes the rows that have misatkes and prints a summary of the sales for a multi-branch retail company.

## Why would someone find it useful?
sales data from different branches can be messey, this program checks each row so it does not have to be rechecked by a manager by hand 

## What problem does it solve?
The program find rows with negative revenue, missing branch ID, or an invalid date and leaves them out while showing the reason they were left out

## What kind of data does it work with?
It works with a CSV file that has five columns: branch_id, transaction_date, customer_tier, item-count and revenue. There is a sample file with some made up data that has a few mistakes so it can tested.

## How is the project easy to build and run?
It only uses tools that come with python so nothing else needs to be installed. The code is split into small files, and each file has its own job which make it easy to read.

## Who did what?
Okuonghae Ikponmwosa Patrick wrote the code, the tests, the README and this document.